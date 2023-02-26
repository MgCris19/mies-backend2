from rest_framework import status, viewsets
from app.balancedScoredCard.serializers import IndicatorSerializer, PerspectiveSerializer, ObjectiveSerializer, BscSerializer

from app.modelBase.response import ResponseData
from app.middleware.mixins import Authentication
from app.modelBase.enum import TYPECODE, MESSAGE

class PerspectiveViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = PerspectiveSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, MESSAGE.NULL, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        perspective_serializer = self.get_serializer(self.get_queryset(), many = True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, perspective_serializer.data, status.HTTP_200_OK)
        
    
    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            perspective_serializer = self.serializer_class(
                self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, perspective_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
    

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            perspective_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if perspective_serializer.is_valid():
                perspective_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, perspective_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk=None):
        try:
            perspective_serializer = self.get_queryset().filter(id=pk).first()
            print(perspective_serializer)
            if perspective_serializer:
                perspective_serializer.state = 'I'
                perspective_serializer.id_user_modified = request.data['id_user_modified']
                perspective_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except :
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)


    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            perspective_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if perspective_serializer.is_valid():
                perspective_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, perspective_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)




class IndicatorViewSet(Authentication, viewsets.ModelViewSet):
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
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, MESSAGE.NULL, status.HTTP_201_CREATED)
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

class ObjectiveViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = ObjectiveSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        print(TYPECODE.SI)
        objective_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, objective_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            objective_serializer = self.serializer_class(
                self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, objective_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, MESSAGE.NULL, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            objective_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if objective_serializer.is_valid():
                objective_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, objective_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            objective_serializer = self.get_queryset().filter(id=pk).first()
            
            if objective_serializer:
                
                objective_serializer.state = 'I'
                objective_serializer.id_user_modified = request.data['id_user_modified']
                objective_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            objective_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if objective_serializer.is_valid():
                objective_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, objective_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
    

class BscViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = BscSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state='A')
        return self.get_serializer().Meta.model.objects.filter(state='A', id=pk).first()

    def list(self, request):
        bsc_serializer = self.get_serializer(self.get_queryset(), many=True)
        return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, bsc_serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            bsc_serializer = self.serializer_class(
                self.get_queryset(pk))
            return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.OK, bsc_serializer.data, status.HTTP_200_OK)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData.Response(TYPECODE.NO, TYPECODE.CREATED, MESSAGE.CREATED, serializer.data, status.HTTP_201_CREATED)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            bsc_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if bsc_serializer.is_valid():
                bsc_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, bsc_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            bsc_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if bsc_serializer.is_valid():
                bsc_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.UPDATE, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.BAD_REQUEST, MESSAGE.BAD_REQUEST, bsc_serializer.errors, status.HTTP_400_BAD_REQUEST)
        return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            bsc_serializer = self.get_queryset().filter(id=pk).first()
            if bsc_serializer:
                bsc_serializer.state = 'I'
                bsc_serializer.id_user_modified = request.data['id_user_modified']
                bsc_serializer.save()
                return ResponseData.Response(TYPECODE.NO, TYPECODE.OK, MESSAGE.DESTROY, MESSAGE.NULL, status.HTTP_200_OK)
            return ResponseData.Response(TYPECODE.SI, TYPECODE.NOT_FOUND, MESSAGE.NOT_FOUND, MESSAGE.NULL, status.HTTP_404_NOT_FOUND)
        except:
            return ResponseData.Response(TYPECODE.SI, TYPECODE.INTERNAL_ERROR, MESSAGE.INTERNAL_ERROR, MESSAGE.NULL, status.HTTP_500_INTERNAL_SERVER_ERROR)