from app.menu.serializers.menu_has_screen_serializers import MenuScreenSerializer
from rest_framework import status, viewsets

from app.modelBase.response import ResponseData
from app.middleware.mixins import Authentication

from app.modelBase.enum import TYPECODE,MESSAGE
from django.db import connection

class MenuScreenViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = MenuScreenSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()
    
    def list(self, request):        
        try:
            menu_has_pantalla_serializer = self.get_serializer(self.get_queryset(), many=True)            
            if menu_has_pantalla_serializer.data:
                print(menu_has_pantalla_serializer.data)
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, menu_has_pantalla_serializer.data, status.HTTP_200_OK)
            else:
                return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.DATA_EMPTY, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        # if self.get_queryset(pk):
        #     menu_has_pantalla_serializer = self.serializer_class(self.get_queryset(pk))
        #     return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, menu_has_pantalla_serializer.data, status.HTTP_200_OK)
        # return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:    
            cursor = connection.cursor() 
            error = []
            for data in request.data:            
                cursor.execute('call insert_menu_has_pantalla (%s, %s,%s)', (data['idMenu'],data['idScreen'],data['id_user_created']))
                result_set = cursor.fetchall()# ((id, nombre, descripcion),(id, nombre, descripcion))
                if result_set[0][1] == '1':
                    error.append(data)                   
                           
            if(error):
                return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.DATA_NOT_SAVE, error, status.HTTP_400_BAD_REQUEST)
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, MESSAGE.NULL, status.HTTP_201_CREATED)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            cursor.close()
    
    def destroy(self, request, pk=None):
        try:
            print(pk)
            cursor = connection.cursor() 
            error = []
            for data in request.data:            
                cursor.execute('call update_menu_has_pantalla (%s, %s,%s,%s)', 
                                (pk,data['idScreen'],data['id_user_modified'], data['state']))
                result_set = cursor.fetchall()
                if result_set[0][1] == '1':
                    error.append(data)                   
            
            print(result_set)               
            print(len(error))               
            if(len(error) != 0):
                return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, error, status.HTTP_400_BAD_REQUEST)
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, MESSAGE.NULL, status.HTTP_200_OK)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            cursor.close()