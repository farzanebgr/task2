from rest_framework import serializers

from productionsApp.models import Products


# Serializer for Products
class ProductsSerializer(serializers.ModelSerializer):
    productsvisit = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Products
        fields = "__all__"
