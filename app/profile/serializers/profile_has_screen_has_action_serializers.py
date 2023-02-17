from app.profile.models import PerfilHasScreenHasAction
from rest_framework import serializers


class ProfileScreenActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilHasScreenHasAction
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'idProfile':instance.idProfile.id,
            'nameProfile':instance.idProfile.name,
            'idScreen':instance.idScreen.id,
            'nameScreen':instance.idScreen.name,
            'idAction':instance.idAction.id,
            'nameAction':instance.idAction.name,
        }