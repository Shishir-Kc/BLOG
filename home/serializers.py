from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_Account , User_content

class UserAccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')


    class Meta:
        model = User_Account
        fields = ['id', 'username', 'profile_pic']

class UserSession(serializers.Serializer):
    
    name = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)


class UserContent(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = User_content
        fields = ['id', 'post_title', 'content', 'content_image', 'created', 'user']

    def get_user(self, obj):
        try:
            user_account = User_Account.objects.get(user=obj.user)
            profile_pic_url = user_account.profile_pic.url if user_account.profile_pic else None
        except User_Account.DoesNotExist:
            profile_pic_url = None

        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'profile_pic': profile_pic_url
        }