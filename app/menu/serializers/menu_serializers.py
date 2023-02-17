from app.menu.models import Menu
from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'name':instance.name,
            'descripcion':instance.descripcion,
            'icono':instance.icono
        }