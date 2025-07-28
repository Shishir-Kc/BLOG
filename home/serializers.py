from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_Account

class UserAccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')


    class Meta:
        model = User_Account
        fields = ['id', 'username', 'profile_pic']
