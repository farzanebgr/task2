from rest_framework import serializers
from userAccountApp.models import User
from orderApp.models import OrderDetail


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_superuser', 'last_login', 'is_staff', 'groups', 'user_permissions', ]


class UserPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password', ]


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = "__all__"
