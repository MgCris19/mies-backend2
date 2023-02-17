from rest_framework import serializers
from app.user.models import Usuario

class LogoutSerializer(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = ['id']