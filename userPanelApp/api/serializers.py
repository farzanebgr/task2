from rest_framework import serializers

from userAccountApp.models import User
from productionsApp.api.serializers import ProductsSerializer
from orderApp.models import OrderDetail, Order
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
    product = ProductsSerializer()

    class Meta:
        model = OrderDetail
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"