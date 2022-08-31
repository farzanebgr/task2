from rest_framework.routers import DefaultRouter
from django.urls import path, include
from orderApp.api.views import AddProductToOrder

urlpatterns = [
    path('add-to-order', AddProductToOrder.as_view({'get': 'list'}), name='add-product-to-order'),
]
