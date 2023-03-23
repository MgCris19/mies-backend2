from rest_framework import status, viewsets
from app.entrepreneur.serializers import EntrepreneurSerializer, PhoneEntrepreneurSerializer, AssociationEntrepreneurSerializer, PhoneTypeSerializer

from app.modelBase.response import ResponseData
from app.middleware.mixins import Authentication
from app.modelBase.enum import TYPECODE,MESSAGE
from rest_framework.decorators import api_view
from rest_framework.response import Response
class EntrepreneurViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = EntrepreneurSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        print(TYPECODE.SI)
        entrepeneur_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, entrepeneur_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            entrepeneur_serializer = self.serializer_class(self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, entrepeneur_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, serializer.data, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            entrepeneur_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if entrepeneur_serializer.is_valid():
                entrepeneur_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, entrepeneur_serializer.errors, status.HTTP_400_BAD_REQUEST)
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
            phoneentrepeneur_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if phoneentrepeneur_serializer.is_valid():
                phoneentrepeneur_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, phoneentrepeneur_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)


class PhoneTypeViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = PhoneTypeSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        print(TYPECODE.SI)
        phonetypeentrepeneur_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, phonetypeentrepeneur_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            phonetypeentrepeneur_serializer = self.serializer_class(self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, phonetypeentrepeneur_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, MESSAGE.NULL, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            phonetypeentrepeneur_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if phonetypeentrepeneur_serializer.is_valid():
                phonetypeentrepeneur_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, phonetypeentrepeneur_serializer.errors, status.HTTP_400_BAD_REQUEST)
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
            phonetypeentrepeneur_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if phonetypeentrepeneur_serializer.is_valid():
                phonetypeentrepeneur_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, phonetypeentrepeneur_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)


class AssociationEntrepreneurViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = AssociationEntrepreneurSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        print(TYPECODE.SI)
        associationentrepeneur_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, associationentrepeneur_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            associationentrepeneur_serializer = self.serializer_class(self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, associationentrepeneur_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, serializer.data, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            associationentrepeneur_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if associationentrepeneur_serializer.is_valid():
                associationentrepeneur_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, associationentrepeneur_serializer.errors, status.HTTP_400_BAD_REQUEST)
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
            associationentrepeneur_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if associationentrepeneur_serializer.is_valid():
                associationentrepeneur_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, associationentrepeneur_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)


class PhoneEntrepreneurViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = PhoneEntrepreneurSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        print(TYPECODE.SI)
        phonetype_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, phonetype_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            phonetype_serializer = self.serializer_class(self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, phonetype_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, MESSAGE.NULL, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            phonetype_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if phonetype_serializer.is_valid():
                phonetype_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, phonetype_serializer.errors, status.HTTP_400_BAD_REQUEST)
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
            phonetype_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if phonetype_serializer.is_valid():
                phonetype_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, phonetype_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

class PhonebyEntrepreneurViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = PhoneEntrepreneurSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', entrepreneur=pk)
    
    def list(self, request):
        print(TYPECODE.SI)
        phonebyent_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, phonebyent_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            phonebyent_serializer = self.serializer_class(self.get_queryset(pk), many=True)
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, phonebyent_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

