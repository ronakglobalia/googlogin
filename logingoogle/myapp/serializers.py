from rest_framework import serializers
from .models import Customuser, Spyfu


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customuser
        fields = ["email", "first_name", "last_name", "password"]

    def create(self, validated_data):

        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializers(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)


