from rest_framework import serializers
from userAccountApp.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_superuser', 'last_login', 'is_staff', 'groups', 'user_permissions', ]
