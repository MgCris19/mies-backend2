from rest_framework import status, viewsets
from app.bond.serializers import BondSerializer

from app.modelBase.response import ResponseData
from app.middleware.mixins import Authentication
from app.modelBase.enum import TYPECODE, MESSAGE

class BondViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = BondSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        print(TYPECODE.SI)
        bond_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, bond_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            bond_serializer = self.serializer_class(
                self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, bond_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, serializer.data, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            bond_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if bond_serializer.is_valid():
                bond_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, bond_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            delete_serializer = self.get_queryset().filter(id=pk).first()
            if delete_serializer:
                delete_serializer.state = 'I'
                delete_serializer.id_user_modified = request.data['id_user_modified']
                delete_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            bond_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if bond_serializer.is_valid():
                bond_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, bond_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)


class BondByEntrepreneurViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = BondSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', entrepreneur=pk)
    
    def list(self, request):
        print(TYPECODE.SI)
        bondbyent_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, bondbyent_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            bondbyent_serializer = self.serializer_class(self.get_queryset(pk), many=True)
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, bondbyent_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)