from rest_framework import serializers
from .models import TypeActivityEconomic, EntrepreneurShipActivityEconomic

class TypeActivityEconomicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeActivityEconomic
        fields = '__all__'
    
class EntrepreneurShipActivityEconomicSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrepreneurShipActivityEconomic
        fields = '__all__'
