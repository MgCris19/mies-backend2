from django.shortcuts import render
from rest_framework import status, viewsets
from app.logGeneral.serializers import logGeneralSerializer
from app.modelBase.response import ResponseData
from app.middleware.mixins import Authentication
from app.modelBase.enum import TYPECODE, MESSAGE

# Create your views here.


class logGeneralViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = logGeneralSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        print(TYPECODE.SI)
        logGeneral_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, logGeneral_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            logGeneralSerializer = self.serializer_class(
                self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, logGeneralSerializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, serializer.data, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            logGeneralSerializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if logGeneralSerializer.is_valid():
                logGeneralSerializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, logGeneralSerializer.data, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, logGeneralSerializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, logGeneralSerializer.data, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        logGeneralSerializer = self.get_queryset().filter(id=pk).first()
        if logGeneralSerializer:
            logGeneralSerializer.state = 'I'
            logGeneralSerializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, logGeneralSerializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            logGeneralSerializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if logGeneralSerializer.is_valid():
                logGeneralSerializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, logGeneralSerializer.data, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, logGeneralSerializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
