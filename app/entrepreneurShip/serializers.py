from rest_framework import serializers
from .models import Entrepreneurship

class EntrepreneurshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneurship
        fields = '__all__'