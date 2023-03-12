from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from app.modelBase.enum import TYPECODE,MESSAGE
from app.entrepreneur.models import Entrepreneur
from django.http import HttpResponse,JsonResponse

@api_view(['POST'])
def getEntrepreneurByName(request):
    # Lógica de la vista personalizada
    mensaje = {"message": "No se encontro ningun registro"}
    
    try:
            search = request.data['search']
            registros = Entrepreneur.objects.filter(entrepreneur__icontains=search,state='A')
            if registros:
                data = {'data': list(registros.values())}
                return Response(data)
            return JsonResponse(mensaje, status=status.HTTP_404_NOT_FOUND)
    except:
            return JsonResponse({"message": "Error de servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)