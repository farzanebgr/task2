from rest_framework import serializers

from productionsApp.models import ProductsBrand, BrandsComments, ProductsCategory, CategoryParent, ProductsTags, \
    Products, ProductGallery, ProductsComments, ProductsRating

# Serializer for Brand
class BrandsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductsBrand
        fields = "__all__"


# Serializer for Brand comments
class BrandsCommentsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    parent = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = BrandsComments
        exclude = ['isActive', ]


# Serializer for Category
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategory
        fields = "__all__"


# Serializer for Parent Category
class CategoryParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryParent
        fields = "__all__"


# Serializer for Tags Products
class ProductsTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsTags
        fields = "__all__"


# Serializer for Products
class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True, many=True)
    brand = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Products
        fields = "__all__"


# Serializer for Products
class ProductsGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = "__all__"

# Serializer for Product
class ProductRatingsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductsRating
        fields = "__all__"

# Serializer for Products comments
class ProductsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsComments
        fields = "__all__"
