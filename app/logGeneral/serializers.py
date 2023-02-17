from dataclasses import field, fields
from rest_framework import serializers
from .models import LogGeneral


class logGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogGeneral
        fields = '__all__'