from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from userAccountApp.models import User
from orderApp.models import OrderDetail
from siteSettingsApp.models import UserPanel

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_superuser', 'last_login', 'is_staff', 'groups', 'user_permissions', ]

class UserPanelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPanel
        fields = "__all__"

class UserPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password', ]


class OrderDetailSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    class Meta:
        model = OrderDetail
        fields = "__all__"
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Products.objects.all(),
        #         fields=['productCount', 'pk']
        #     )
        #     ]