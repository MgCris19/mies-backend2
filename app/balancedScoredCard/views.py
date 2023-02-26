from rest_framework import status, viewsets

from app.balancedScoredCard.serializers import PerspectiveSerializer, IndicatorSerializer, ObjectiveSerializer

from app.modelBase.response import ResponseData
from app.middleware.mixins import Authentication
from app.modelBase.enum import TYPECODE, MESSAGE
# Create your views here.


class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        indicator_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, indicator_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            indicator_serializer = self.serializer_class(
                self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, indicator_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, serializer.data, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            indicator_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if indicator_serializer.is_valid():
                indicator_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, indicator_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            indicator_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if indicator_serializer.is_valid():
                indicator_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, indicator_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            indicator_serializer = self.get_queryset().filter(id=pk).first()
            if indicator_serializer:
                indicator_serializer.state = 'I'
                indicator_serializer.id_user_modified = request.data['id_user_modified']
                indicator_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)
