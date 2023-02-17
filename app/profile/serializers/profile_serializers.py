from app.profile.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'name':instance.name,
            'descripcion':instance.descripcion
        }