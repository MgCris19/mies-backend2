from app.menu.models import Screen
from rest_framework import serializers


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'name':instance.name,
            'descripcion':instance.descripcion,
            'icono':instance.icono,
            'uri':instance.uri
        }