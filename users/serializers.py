from rest_framework import serializers

from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    class Meta:
        model = UserProfile
        fields = [
            'username',
            'user_type',
            'full_name',
            'phone_number',
            'address',
            'buyer_type',
            'latitude',
            'longitude'
        ]

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['username', 'email', 'profile']