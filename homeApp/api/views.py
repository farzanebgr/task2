# Import directly from rest_framework
from rest_framework import viewsets
# Import serializers from serializers' file
from homeApp.api import serializers
# Import models from apps
from siteSettingsApp import models
from productionsApp.models import Products


# Show all sliders and Retrieve Update Destroy APIView a particular slider
class IndexSliderDetailsVS(viewsets.ModelViewSet):
    queryset = models.Slider.objects.all()
    serializer_class = serializers.SliderSerializer


# Show the latest products and Retrieve Update Destroy APIView a particular product
class LatestProductsDetailsVS(viewsets.ModelViewSet):
    queryset = Products.objects.filter(isActive=True, isDelete=False).all()
    serializer_class = serializers.ProductsSerializer


# Show site setting model and Retrieve Update Destroy APIView a particular setting model
class AboutUsDetailsVS(viewsets.ModelViewSet):
    queryset = models.settingModel.objects.filter(isMainSettings=True).all()
    serializer_class = serializers.AboutUsSerializer


# Show site setting model and Retrieve Update Destroy APIView a particular setting model
class SiteHeaderPartialVS(viewsets.ModelViewSet):
    queryset = models.settingModel.objects.filter(isMainSettings=True).all()
    serializer_class = serializers.SiteHeaderSerializer


# Show site setting model and Retrieve Update Destroy APIView a particular setting model
class SiteFooterPartialVS(viewsets.ModelViewSet):

    queryset = models.footerLink.objects.all()
    serializer_class = serializers.SiteFooterPartialAV

