from app.action.models import Action
from rest_framework import serializers


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'name':instance.name,
            'descripcion':instance.descripcion
        }