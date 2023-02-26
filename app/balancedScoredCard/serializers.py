from rest_framework import serializers
from .models import Perspective,Objective, Indicator, Bsc

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
      
class BscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bsc
        fields = '__all__' 