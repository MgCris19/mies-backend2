from django.shortcuts import render
from rest_framework import status, viewsets
from app.entrepreneurcourses.serializers import EntrepreneurCourseSerializer

from app.modelBase.response import ResponseData
from app.middleware.mixins import Authentication

from app.modelBase.enum import TYPECODE,MESSAGE

class EntrepreneurCoursesViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = EntrepreneurCourseSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()


    def list(self, request):
        entrepreneurcoursesSerializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, entrepreneurcoursesSerializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            entrepreneurcoursesSerializer = self.serializer_class(self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, entrepreneurcoursesSerializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, serializer.data, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        if self.get_queryset(pk):
            entrepreneurcoursesSerializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if entrepreneurcoursesSerializer.is_valid():
                entrepreneurcoursesSerializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, entrepreneurcoursesSerializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk=None):
        try:
            entrepreneurcoursesSerializer = self.get_queryset().filter(id=pk).first()
            if entrepreneurcoursesSerializer:
                entrepreneurcoursesSerializer.delete()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)    



    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            entrepreneurcoursesSerializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if entrepreneurcoursesSerializer.is_valid():
                entrepreneurcoursesSerializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, entrepreneurcoursesSerializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
    
