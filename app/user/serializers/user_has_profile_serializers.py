from app.user.models import UserHasProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHasProfile
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'idUser':instance.idUser.id,
            'nameUser':instance.idUser.names,
            'idProfile':instance.idProfile.id,
            'nameProfile':instance.idProfile.name
        }