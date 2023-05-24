from rest_framework import serializers
from django.core.validators import MinLengthValidator
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(
        write_only=True,
        min_length=5,
        validators=[MinLengthValidator(5)],
        required=False
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if 'password' in data or 'confirm_password' in data:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "password and confirm_password do not match!"
                )

        if User.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("user with name already exists!")

        return data

    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create(name=name, email=email)
        user.set_password(password)
        user.save()

        return user
