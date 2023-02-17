from rest_framework.authentication import get_authorization_header
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from app.middleware.authentication import ExpiringTokenAuthentication

from app.modelBase.enum import TYPECODE, MESSAGE
from app.modelBase.response import ResponseData
import json
from django.db import connection
#  cursor = connection.cursor() 
#         cursor.execute('call accionesMenu(%s,%s)', (idPerfil,idPantalla))                           
#         result_set2 = cursor.fetchall()                
#         cursor.close()

class Authentication(object):
    user = None,
    user_token_expired = False
        
    def lista(self, data, method, id):
        array = []
        for d in data:
            if method == 'POST':                        
                d['id_user_created'] = id
            if (method == 'PUT') or (method == 'PATCH'):
                print(method)
                d['id_user_modified'] = id
            if (method == 'DELETE'):
                d['id_user_modified'] = id 
            array.append(d)
        return array

    def objeto(self, data,method, id):
        if method == 'POST':                        
            data['id_user_created'] = id
        if (method == 'PUT') or (method == 'PATCH'):
            print(method)
            data['id_user_modified'] = id
        if (method == 'DELETE'):
            data['id_user_modified'] = id         
        return data

    def get_currrent_path(self, request):
        try:
            # request.get_full_path(),
            # accion = request.headers['Accion']
            # pantalla = request.headers['Pantalla']
            # cursor = connection.cursor() 
            # print(accion, '-',pantalla,'-',id)
            # cursor.execute('call verificar_accion (%s,%s,%s)',(accion, id, pantalla))                           
            # result_set = cursor.fetchall()                
            # cursor.close()
            # if result_set[0][0] == None:
            #     pase = 0
            # else:
            #     pase = 1
            return  request.method
        except:
            return ResponseData.Response(TYPECODE.SI,TYPECODE.UNAUTHORIZED, MESSAGE.UNAUTHORIZED, {"expired":self.user_token_expired}, status.HTTP_401_UNAUTHORIZED)
            
    def get_user(self, request):
        # notToken = self.get_currrent_path(request)
        token = get_authorization_header(request)        
        if token:
            try:
                token = token.decode()               
                token_expire = ExpiringTokenAuthentication()
                user, token, message, self.user_token_expired = token_expire.authenticate_credentials(
                    token)                
                if user != None and token != None:
                    self.user = user
                    return user
                return message
            except:
                return None
        return None

    # este es el primer método que ejecuta django
    def dispatch(self, request, *args, **kwargs):
        try:
            print("dispatch")
            user = self.get_user(request)
            method = self.get_currrent_path(request)   
            # print(path,method,pase)     
            if user is not None:
                # if pase != 0:
                if type(user) == str:
                    return ResponseData.Response(TYPECODE.SI,TYPECODE.UNAUTHORIZED, user, {"expired":self.user_token_expired}, status.HTTP_401_UNAUTHORIZED)
                if not self.user_token_expired:
                    try:
                        data = json.loads(request.body.decode ('utf-8'))                                                            
                        if isinstance(data, list):
                            print( "dispatch data==> ",isinstance(data, list))
                            data = self.lista(data, method, user.id)
                        elif isinstance(data, dict):
                            print( "dispatch data==> ",isinstance(data, dict))
                            data = self.objeto(data, method, user.id)
                                        
                        request._body = bytes(json.dumps(data), encoding='utf-8')   

                        print( "dispatch ==> ",request._body )                             
                    except:
                        print("Para que no muera")
                    return super().dispatch(request, *args, **kwargs)    
            return ResponseData.Response(TYPECODE.SI,TYPECODE.UNAUTHORIZED, MESSAGE.UNAUTHORIZED, {"expired":self.user_token_expired}, status.HTTP_401_UNAUTHORIZED)
        except:
            return ResponseData.Response(TYPECODE.SI,TYPECODE.UNAUTHORIZED, MESSAGE.UNAUTHORIZED, MESSAGE.NULL, status.HTTP_401_UNAUTHORIZED)
