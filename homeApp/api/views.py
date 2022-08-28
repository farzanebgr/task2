from rest_framework import generics
from rest_framework import viewsets
from homeApp.api.serializers import SliderSerializer, ProductsSerializer, AboutUsSerializer
from django.db.models import Count
from django.shortcuts import render
from siteSettingsApp.models import settingModel, footerLinkBox, Slider
from productionsApp.models import Products


# Show all sliders and Retrieve Update Destroy APIView a particular slider
class IndexSliderDetailsAV(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


# Show a particular active product and Retrieve Update Destroy APIView
class LatestProductsDetailsAV(viewsets.ModelViewSet):
    queryset = Products.objects.filter(isActive=True, isDelete=False).all()
    serializer_class = ProductsSerializer


# Show a particular most visit product and Retrieve Update Destroy APIView
class MostVisitProductsDetailsAV(viewsets.ModelViewSet):
    queryset = Products.objects.filter(isActive=True, isDelete=False).annotate(
        visit_count=Count('productsvisit')).all()
    serializer_class = ProductsSerializer


# Show particular active site setting model and Retrieve Update Destroy APIView
class AboutUsDetailsAV(viewsets.ModelViewSet):
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
