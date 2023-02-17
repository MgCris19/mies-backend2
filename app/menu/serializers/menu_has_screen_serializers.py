from app.menu.models import MenuHasScreen
from rest_framework import serializers


class MenuScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuHasScreen
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'idMenu': instance.idMenu.id,
            'nombreMenu': instance.idMenu.name,
            'idScreen': instance.idScreen.id,
            'nombreScreen': instance.idScreen.name,
        }
