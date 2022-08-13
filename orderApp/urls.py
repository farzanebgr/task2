from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order', views.addProductToOrder, name='add-product-to-order')
]
