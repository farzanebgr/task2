from rest_framework import viewsets
from homeApp.api.serializers import SliderSerializer, ProductsSerializer, AboutUsSerializer, SiteHeaderSerializer,\
    SiteFooterPartialAV
from django.db.models import Count
from siteSettingsApp.models import settingModel, Slider, footerLink
from productionsApp.models import Products


# Show all sliders and Retrieve Update Destroy APIView a particular slider
class IndexSliderDetailsVS(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


# Show the latest products and Retrieve Update Destroy APIView a particular product
class LatestProductsDetailsVS(viewsets.ModelViewSet):
    queryset = Products.objects.filter(isActive=True, isDelete=False).all()
    serializer_class = ProductsSerializer


# Show site setting model and Retrieve Update Destroy APIView a particular setting model
class AboutUsDetailsVS(viewsets.ModelViewSet):
    queryset = settingModel.objects.filter(isMainSettings=True).all()
    serializer_class = AboutUsSerializer


# Show site setting model and Retrieve Update Destroy APIView a particular setting model
class SiteHeaderPartialVS(viewsets.ModelViewSet):
    queryset = settingModel.objects.filter(isMainSettings=True).all()
    serializer_class = SiteHeaderSerializer


# Show site setting model and Retrieve Update Destroy APIView a particular setting model
class SiteFooterPartialVS(viewsets.ModelViewSet):

    queryset = footerLink.objects.all()
    serializer_class = SiteFooterPartialAV

