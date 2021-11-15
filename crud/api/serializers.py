from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import ModelUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUser
        fields = "__all__"


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUser
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser',)
        extra_kwargs = {"is_superuser": {"read_only": True}, "last_login": {"read_only": True}}


class WriteOnlyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        validators=[RegexValidator(regex=r'^(?=.*[A-Z])(?=.*\d).{8,}$', message='Не правильно задан пароль')]
    )

    class Meta:
        model = ModelUser
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'is_active',)

    def create(self, validated_data):
        user = ModelUser.objects.create_user(**validated_data)
        return user

