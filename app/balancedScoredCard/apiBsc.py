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
            consulta = "select tb.* from tbl_bsc tb where tb.Id_emprendedor_id = (%s) and tb.state = 'A'"
            filtro = search
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

@api_view(['POST'])
def getControlByEntrepreneur(request):
    # Lógica de la vista personalizada
    mensaje = {"message": "No se encontro ningun registro"}
    
    try:
            search = request.data['search']
           # consulta = "select tb.* from tbl_bsc tb where tb.Id_emprendedor_id = (%s) and tb.state = 'A'"
            consulta = "select tc.* from tbl_control tc join tbl_bsc tb on tb.id = tc.bsc_id where tb.Id_emprendedor_id = (%s) and tc.state = 'A' and tb.state = 'A'"
            filtro = search
            registros = Control.objects.raw(consulta,[filtro])
            if registros:
                
                # Serializar los resultados en formato JSON
                resultados_json = []
                resBsc = []
                for resultado in registros:
                    resBsc = {'id_bsc': 
                    resultado.bsc.id,'peso':resultado.bsc.peso,'peso_avance':resultado.bsc.peso_avance
                    ,'peso_alcanzado':resultado.bsc.peso_alcanzado,'id_objetivo':resultado.bsc.Id_Objetivo.id,
                    'objetivo':resultado.bsc.Id_Objetivo.name,'id_indicador':resultado.bsc.Id_Indicator.id,
                    'nombre_indicador':resultado.bsc.Id_Indicator.name,
                    'id_emprendedor':resultado.bsc.Id_emprendedor.id,'emprendedor':resultado.bsc.Id_emprendedor.entrepreneur}
                    resultados_json.append({
                         'id': resultado.id,
                         'state': resultado.state,
                         'created_date': resultado.created_date,
                         'modified_date': resultado.modified_date,
                         'id_user_created': resultado.id_user_created,
                         'id_user_modified': resultado.id_user_modified,
                         'actividad':resultado.actividad,
                         'fecha_inicio':resultado.fecha_inicio,
                         'fecha_fin':resultado.fecha_fin,
                         'peso_actividad':resultado.peso_actividad,
                         'avance':resultado.avance,
                         'bsc':resBsc,
        # ... y así sucesivamente para cada campo que se desee incluir
                    })

                return JsonResponse({'data': resultados_json})
            return JsonResponse(mensaje, status=status.HTTP_404_NOT_FOUND)
    except:
            return JsonResponse({"message": "Error de servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)