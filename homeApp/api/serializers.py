from rest_framework import serializers

from siteSettingsApp.models import Slider, settingModel
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
