from rest_framework import viewsets
from orderApp.api.serializers import OrderDetailSerializer
from django.db.models import Count

from productionsApp.models import Products
from orderApp.models import Order, OrderDetail


class AddProductToOrder(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
