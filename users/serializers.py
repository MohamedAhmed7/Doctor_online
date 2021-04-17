from rest_framework import serializers
from users.models import CustomUser


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'date_joined']

class userCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

class userLoginSerializer(serializers.ModelSerializer):
     class Meta:
        model = CustomUser
        fields = ['username','password', 'user_type']