from rest_framework import serializers
from .models import Perspective,Objective, Indicator, Bsc, Control

class PerspectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perspective
        fields = '__all__'

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'  
      
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['perspective'] = {'id_perspective': 
        instance.perspective.id,'name':instance.perspective.name}
        ret['indicator'] = {'id_indicator': 
        instance.indicator.id,'name':instance.indicator.name}
        return ret

class BscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bsc
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['objetivo'] = {'id_objetivo': 
        instance.Id_Objetivo.id,'name':instance.Id_Objetivo.name}
        ret['perspectiva']= {'id_perspectiva': 
        instance.Id_Objetivo.perspective.id,'name':instance.Id_Objetivo.perspective.name}
        ret['indicador'] = {'id_indicador': 
        instance.Id_Indicator.id,'name':instance.Id_Indicator.name}
        ret['emprendedor'] = {'id_emprendedor': 
        instance.Id_emprendedor.id,'name':instance.Id_emprendedor.user.names}
        return ret
        
class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['bsc'] = {'id_bsc': 
        instance.bsc.id,'peso':instance.bsc.peso,
        'peso_avance':instance.bsc.peso_avance,
        'peso_alcanzado':instance.bsc.peso_alcanzado,
        'id_objetivo':instance.bsc.Id_Objetivo.id,
        'id_indicador':instance.bsc.Id_Indicator.id,
        'nombre_indicador':instance.bsc.Id_Indicator.name,
        'id_emprendedor':instance.bsc.Id_emprendedor.id}

        return ret