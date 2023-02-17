from wsgiref import validate
from rest_framework import serializers
from app.user.models import Usuario

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email','names','id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['created_date', 'last_login','modified_date']

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'state':instance.state,
            'email':instance.email,
            'names':instance.names,
            'identify':instance.identify            
        }

    def create(self, validated_data):
        print(validated_data)
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        try:            
            if validated_data['password'] != None:   
                update_user.set_password(validated_data['password'])
        except:
            print('error')

        print(update_user)
        update_user.save()
        return update_user
