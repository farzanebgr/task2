from rest_framework import serializers
from star_ratings.models import UserRating

from productionsApp import models

# Serializer for Brand
class BrandsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.ProductsBrand
        fields = "__all__"


# Serializer for Brand comments
class BrandsCommentsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    parent = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.BrandsComments
        exclude = ['isActive', ]


# Serializer for Category
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductsCategory
        fields = "__all__"


# Serializer for Parent Category
class CategoryParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryParent
        fields = "__all__"


# Serializer for Tags Products
class ProductsTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductsTags
        fields = "__all__"


# Serializer for Products
class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True, many=True)
    brand = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Products
        fields = "__all__"


# Serializer for Products
class ProductsGallerySerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    class Meta:
        model = models.ProductGallery
        fields = "__all__"

# Serializer for Product
class ProductRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = "__all__"

# Serializer for Products comments
class ProductsCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product = ProductsSerializer()
    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.ProductsComments
        fields = "__all__"


# Serializer for Products comments
class CreateProductsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductsComments
        fields = "__all__"


# Serializer for Products comments
class CreateBrandCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrandsComments
        fields = "__all__"
