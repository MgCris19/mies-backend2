from django.contrib.sessions.models import Session
from datetime import datetime
from app.menu.views.menu_views import MenuViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from app.user.serializers.user_serializers import UserTokenSerializer
from app.modelBase.response import ResponseData
from app.login.serializers import LogoutSerializer

from app.modelBase.enum import TYPECODE, MESSAGE
from django.db import connection


class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        try:
            username = request.GET.get('username')
            try:
                user_token = Token.objects.get(
                    user=UserTokenSerializer().Meta.model.objects.filter(username=username).first()
                )
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, {'token': user_token.key}, status.HTTP_200_OK)
            except:
                return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_CREDENTIALS, MESSAGE.NULL, status.HTTP_400_BAD_REQUEST)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)


class Login(ObtainAuthToken):

    def acciones(self, idPerfil, idPantalla):
        cursor = connection.cursor() 
        cursor.execute('call accionesMenu(%s,%s)', (idPerfil,idPantalla))                           
        result_set = cursor.fetchall()  
        acciones = []
        if len(result_set) > 0:
            cursor.close()

            for it2 in result_set:
                acciones.extend(it2)
        return acciones

    def pantallas(self,it):
        pantalla = {}        
        acciones = self.acciones(it[0],it[5])
                                                        
        pantalla.update(
            {
                
                'id':it[5],
                'pantalla': it[6],
                'icono':it[7],
                'url':it[8],
                'acciones': acciones.copy()
                
            }
        )
        acciones.clear()                    
        return pantalla 

    def menus(self, it):        
        pantallas = []
        menu = {}
        pantallas.append(self.pantallas(it))
       
        
        menu.update(
            {
                
                'menu': it[3],
                'icono':it[4],
                'pantallas':pantallas.copy()
                
            }
        )
        return menu

    def perfiles(self, email):
        try:
            cursor = connection.cursor() 
            cursor.execute('call obtener_usuario_perfil(%s,%s)', (email, 0))                           
            result_set = cursor.fetchall()    
            pantallas = []                        
            menus = []
            menu = {}
            
            if len(result_set) >0:
                                        
                # perfiles = []
                # perfil = {}           
                # vp = result_set[0][5]
                vm = result_set[0][2]

                for it in result_set:                               
                    if vm == it[2]: 
                        pantallas.append(self.pantallas(it))            
                        menu.update(
                            {
                            
                                'menu': it[3],
                                'icono':it[4],
                                'pantallas':pantallas.copy()
                            
                            }
                        )                        
                    else:
                        # menus.pop() 
                        menus.append(menu.copy())                                
                        vm = it[2]
                        pantallas.clear()
                        pantallas.append(self.pantallas(it))                
                        menu.update(
                            {
                                
                                'menu': it[3],
                                'icono':it[4],
                                'pantallas':pantallas.copy()
                            
                            }
                        )                
                    # menus.append(menu.copy())
                menus.append(menu.copy())                                                                                 
                # print("menu =>", menus)  
                # if len(perfil) == 0:
                #     menus.pop()
                #     perfil.update(
                #         {
                #             result_set[0][1]:{
                #                 'id':result_set[0][0], 
                #                 'perfil':result_set[0][1],
                #                 'menus':menus
                #             }
                #         }
                #     )  
                # perfiles.append(perfil)
                # perfiles.append(menus)                        
            return menus            
        except:
            raise ValueError("El usuario no posee un perfil/menu asignado")
            # return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            cursor.close()

    def post(self, request, *args, **kwargs):       
        try:            
            print("login")
            key = None
            login_serializer = self.serializer_class(
                data=request.data, context={'request': request})
            if not login_serializer.is_valid():
                return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_LOGIN, MESSAGE.NULL, status.HTTP_400_BAD_REQUEST)
            else:
                user = login_serializer.validated_data['user']
                # in_session
                token = Token.objects.filter(user=user.id)
                print(token)
                for t in token:
                    key = t.key
                if key is None:
                    if user.state == 'A':
                        token, created = Token.objects.get_or_create(user=user)
                        user_serializer = UserTokenSerializer(user)
                        if created:
                            email = user_serializer.data['email']
                            # menus = []
                            # menus.append(self.perfiles(email))
                            menus = self.perfiles(email)
                            
                                                         
                            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.LOGIN,
                                                        {
                                                            'token': token.key,
                                                            'user': user_serializer.data,
                                                            'menus':menus
                                                        }, status.HTTP_201_CREATED)
                        else:
                            all_session = Session.objects.filter(
                                expire_date__gte=datetime.now())
                            if all_session.exists():
                                for session in all_session:
                                    session_data = session.get_decoded()
                                    if user.id == int(session_data.get('_auth_user_id')):
                                        session.delete()
                            token.delete()
                            token = token.objects.create(user)                            

                            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.LOGIN,
                                                        {
                                                            'token': token.key,
                                                            'user': user_serializer.data
                                                        }, status.HTTP_201_CREATED)
                    else:
                        return ResponseData.Response(TYPECODE.SI, TYPECODE.UNAUTHORIZED, MESSAGE.NOT_SESSION, MESSAGE.NULL, status.HTTP_401_UNAUTHORIZED)
                else:
                    return ResponseData.Response(TYPECODE.SI, TYPECODE.CONFLICT, MESSAGE.ON_SESSION, MESSAGE.NULL, status.HTTP_409_CONFLICT)
        except ValueError as e:
            print(e)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR,  MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)       
            

class Logout(APIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        try:
            logout_serializer = self.serializer_class(
                data=request.data, context={'request': request})
            if logout_serializer.is_valid:
                user = request.data['id']
                token = Token.objects.filter(user=int(user)).first()
                if token:
                    all_session = Session.objects.filter(
                        expire_date__gte=datetime.now())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, {'token_message': MESSAGE.TOKEN_MESSAGE,
                                                                                        'session_message': MESSAGE.SESSION_MESSAGE}, status.HTTP_200_OK)
                return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.NOT_FOUND_USER, MESSAGE.NULL, status.HTTP_400_BAD_REQUEST)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.CONFLICT, MESSAGE.NOT_FOUND_TOKEN, MESSAGE.NULL, status.HTTP_409_CONFLICT)