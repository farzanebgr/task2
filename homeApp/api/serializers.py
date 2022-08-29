from rest_framework import serializers

from siteSettingsApp.models import Slider, settingModel, footerLink
from productionsApp.models import Products


# Serializer for Sliders in index page
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


# Serializer for Products
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


# Serializer for settingModel
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = settingModel
        fields = "__all__"


# Serializer for site header
class SiteHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = settingModel
        exclude = ['siteMap', 'siteRights']


# Serializer for site footer
class SiteFooterPartialAV(serializers.ModelSerializer):
    footerLinkRelation = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = footerLink
        fields = "__all__"
