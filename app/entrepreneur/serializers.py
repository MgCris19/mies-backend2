from rest_framework import serializers
from .models import Entrepreneur, PhoneEntrepreneur, AssociationEntrepreneur, PhoneType

class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = '__all__'

class PhoneEntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneEntrepreneur
        fields = '__all__'

class AssociationEntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociationEntrepreneur
        fields = '__all__'

class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneType
        fields = '__all__'