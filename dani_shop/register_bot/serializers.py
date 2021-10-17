from rest_framework import serializers
from register_bot.models import Profile


class RegisterUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=64)
    origin = serializers.ChoiceField(Profile.ORIGIN_CHOICES, allow_null=True, required=False)
