from dataclasses import field, fields
from rest_framework import serializers
from .models import Observations


class observationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observations
        fields = '__all__'