from app.menu.serializers.screen_serializers import ScreenSerializer
from rest_framework import status, viewsets

from app.modelBase.response import ResponseData
from app.middleware.mixins import Authentication

from app.modelBase.enum import TYPECODE,MESSAGE

class ScreenViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = ScreenSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        try:
            screen_serializer = self.get_serializer(self.get_queryset(), many=True)
            if screen_serializer.data:
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, screen_serializer.data, status.HTTP_200_OK)
            else:
                return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.DATA_EMPTY, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                screen_serializer = self.serializer_class(self.get_queryset(pk))
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, screen_serializer.data, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():                
                id = {"id":serializer.save().id}   
                return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, id, status.HTTP_201_CREATED)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)   
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                screen_serializer = self.serializer_class(
                    self.get_queryset(pk), data=request.data)
                if screen_serializer.is_valid():
                    screen_serializer.save()
                    return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
                return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, screen_serializer.errors, status.HTTP_400_BAD_REQUEST)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def partial_update(self, request, pk=None):
        # if self.get_queryset(pk):
        #     screen_serializer = self.serializer_class(
        #         self.get_queryset(pk), data=request.data)
        #     if screen_serializer.is_valid():
        #         screen_serializer.save()
        #         return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
        #     return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, screen_serializer.errors, status.HTTP_400_BAD_REQUEST)
        # return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            screen = self.get_queryset().filter(id=pk).first()
            if screen:
                screen.state = 'I'
                screen.id_user_modified = request.data['id_user_modified']
                screen.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)