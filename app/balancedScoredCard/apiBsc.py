from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from app.modelBase.enum import TYPECODE,MESSAGE
from app.balancedScoredCard.models  import Perspective, Indicator, Objective, Bsc, Control
from django.http import HttpResponse,JsonResponse
from app.balancedScoredCard.serializers import IndicatorSerializer, PerspectiveSerializer, ObjectiveSerializer, BscSerializer, ControlSerializer

@api_view(['POST'])
def getBscByName(request):
    # Lógica de la vista personalizada
    mensaje = {"message": "No se encontro ningun registro"}
    
    try:
            search = request.data['search']
            consulta = "select tb.* from tbl_bsc tb join tbl_objetivo obj on obj.id  = tb.Id_Objetivo_id where UPPER(obj.name)  like UPPER(%s) and tb.state = 'A'"
            filtro = '%'+search+'%'
            registros = Bsc.objects.raw(consulta,[filtro])

            if registros:
                
                # Serializar los resultados en formato JSON
                resultados_json = []
                resObj = []
                resEmp = []
                resInd = []
                resPers = []
                for resultado in registros:
                    resObj = {'id_objetivo': 
                    resultado.Id_Objetivo.id,'name':resultado.Id_Objetivo.name}
                    resPers = {'id_perspectiva': 
                    resultado.Id_Objetivo.perspective.id,'name':resultado.Id_Objetivo.perspective.name}
                    resInd = {'id_indicador': 
                    resultado.Id_Indicator.id,'name':resultado.Id_Indicator.name}
                    resEmp = {'id_emprendedor': 
                    resultado.Id_emprendedor.id,'name':resultado.Id_emprendedor.entrepreneur}
                    resultados_json.append({
                         'id': resultado.id,
                         'state': resultado.state,
                         'created_date': resultado.created_date,
                         'modified_date': resultado.modified_date,
                         'id_user_created': resultado.id_user_created,
                         'id_user_modified': resultado.id_user_modified,
                         'peso': resultado.peso,
                         'peso_avance': resultado.peso_avance,
                         'peso_alcanzado': resultado.peso_alcanzado,
                         'Id_Objetivo':resObj,
                         'Id_Indicator':resInd,
                         'Id_emprendedor':resEmp,
                         'perspectiva':resPers,
        # ... y así sucesivamente para cada campo que se desee incluir
                    })

                return JsonResponse({'data': resultados_json})
            return JsonResponse(mensaje, status=status.HTTP_404_NOT_FOUND)
    except:
            return JsonResponse({"message": "Error de servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)