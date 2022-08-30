from rest_framework import serializers

from productionsApp.models import ProductsBrand, ProductsCategory, Products, ProductGallery, ProductsComments


# Serializer for Brand
class BrandsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductsBrand
        fields = "__all__"


# Serializer for Category
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategory
        fields = "__all__"


# Serializer for Products
class ProductsSerializer(serializers.ModelSerializer):
    productsvisit = serializers.StringRelatedField(read_only=True, many=True)
    category = serializers.StringRelatedField(read_only=True, many=True)
    brand = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Products
        fields = "__all__"


# Serializer for Products
class ProductsGallerySerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductGallery
        fields = "__all__"


# Serializer for Products comments
class ProductsCommentSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    parent = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductsComments
        fields = "__all__"