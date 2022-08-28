from rest_framework import generics

from homeApp.api.serializers import SliderSerializer, ProductsSerializer, AboutUsSerializer
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from siteSettingsApp.models import settingModel, footerLinkBox, Slider
from productionsApp.models import Products
from utils.convertors import group_list


# Show all active sliders and create new one
class IndexSliderAV(generics.ListCreateAPIView):
    queryset = Slider.objects.filter(isActive=True)
    serializer_class = SliderSerializer


# Show a particular active sliders and Retrieve Update Destroy APIView
class IndexSliderDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


# Show 12 active products and create new one
class LatestProductsAv(generics.ListCreateAPIView):
    queryset = Products.objects.filter(isActive=True, isDelete=False)[:12]
    serializer_class = ProductsSerializer


# Show a particular active product and Retrieve Update Destroy APIView
class LatestProductsDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.filter(isActive=True, isDelete=False).all()
    serializer_class = ProductsSerializer


# Show 12 most visit products and create new one
class MostVisitProductsAV(generics.ListCreateAPIView):
    queryset = Products.objects.filter(isActive=True, isDelete=False).annotate(
        visit_count=Count('productsvisit')).order_by('-productsvisit')[:12]
    serializer_class = ProductsSerializer


# Show a particular most visit product and Retrieve Update Destroy APIView
class MostVisitProductsDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.filter(isActive=True, isDelete=False).annotate(
        visit_count=Count('productsvisit')).all()
    serializer_class = ProductsSerializer


# Show active site setting model and create new one
class AboutUsAV(generics.ListCreateAPIView):
    queryset = settingModel.objects.filter(isMainSettings=True).all()
    serializer_class = AboutUsSerializer


# Show particular active site setting model and Retrieve Update Destroy APIView
class AboutUsDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = settingModel.objects.filter(isMainSettings=True).all()
    serializer_class = AboutUsSerializer


def siteHeaderPartial(request):
    settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
    context = {
        'settings': settings
    }
    return render(request, 'shared/header.html', context)


def siteFooterPartial(request):
    settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
    footer_link_boxes = footerLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set

    context = {
        'settings': settings,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/footer.html', context)
