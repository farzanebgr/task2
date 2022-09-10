# import directly from rest framework
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# import from rest framework. something
from rest_framework.response import Response

# import from internal apps
from productionsApp.api.pagination import BrandListPagination, ProductListPagination
from productionsApp.api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from productionsApp.api import serializers
from productionsApp.api.throttling import BrandCommentsThrottle, ProductCommentsThrottle
# import models from productionsApp
from productionsApp.models import ProductsBrand, BrandsComments, ProductsCategory, CategoryParent, ProductsTags, \
    Products, ProductsComments, ProductGallery
from star_ratings.models import UserRating


# Show all Brands and create a new one by permission admin
class BrandsVS(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly,]
    queryset = ProductsBrand.objects.all()
    serializer_class = serializers.BrandsSerializer
    pagination_class = BrandListPagination

    def create(self, request, *args, **kwargs):
        serializer = serializers.BrandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# retrieve a Particular Brand and update and destroy a Particular Brand by permission admin
class BrandDetailsVS(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly,]
    queryset = ProductsBrand.objects.all()
    serializer_class = serializers.BrandsSerializer

    def retrieve(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        brand = ProductsBrand.objects.filter(pk=pk).first()
        serializer = serializers.BrandsSerializer(brand)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        brand = ProductsBrand.objects.filter(pk=pk).first()
        serializer = serializers.BrandsSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        brand = ProductsBrand.objects.filter(pk=pk).first()
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Show All Brand Comments
class BrandCommentsGL(generics.ListAPIView):
    serializer_class = serializers.BrandsCommentsSerializer
    throttle_classes = [ProductCommentsThrottle,]

    def get_queryset(self):
        brand = self.kwargs['id']
        comments = BrandsComments.objects.filter(brand_id=brand, brand__haveComments=True).all()
        if comments is None:
            return Response(serializers.ValidationError({'error':'Brand comments are closed!!!'}))
        return comments

# Show a Particular Brand Comment
class BrandCommentGR(generics.RetrieveAPIView):
    serializer_class = serializers.BrandsCommentsSerializer

    def get_queryset(self):
        brand = self.kwargs['id']
        pk = self.kwargs['pk']
        comment = BrandsComments.objects.filter(brand_id=brand, pk=pk).all()
        if comment is not []:
            return comment
        return Response({'error': 'Brand comment are not available!!!'})


# Create Brand Comment by Auth
class CreateBrandCommentGC(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.CreateBrandCommentSerializer
    throttle_classes = [BrandCommentsThrottle,]

    def create(self, request, *args, **kwargs):
        serializer = serializers.CreateBrandCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# Show, update and destroy a Brand Comment by owner ...
class ChangeBrandCommentGRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly,]
    serializer_class = serializers.CreateBrandCommentSerializer
    throttle_classes = [BrandCommentsThrottle,]

    def retrieve(self, request, *args, **kwargs):
        brand = self.kwargs['id']
        pk = self.kwargs['pk']
        comment = BrandsComments.objects.filter(brand_id=brand,pk=pk,user_id=request.user.id).first()
        serializer = serializers.CreateBrandCommentSerializer(comment)
        if serializer is None:
            return Response(serializers.ValidationError({'error': 'Product comments are closed!!!'}))
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        brand=self.kwargs['id']
        comment = BrandsComments.objects.filter(brand_id=brand,user_id=request.user.id).first()
        serializer = serializers.CreateBrandCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        brand = self.kwargs['id']
        comment = BrandsComments.objects.filter(brand_id=brand, user_id=request.user.id).first()
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Filter products by brand
class BrandFilteringGA(generics.ListAPIView):
    serializer_class = serializers.BrandsSerializer
    queryset = ProductsBrand

    def get_queryset(self):
        brand_name = self.kwargs['brand']
        if brand_name is not None:
            brand = Products.objects.filter(brand__titleEN=brand_name)
            return brand
        else:
            return Response(serializers.ValidationError({'error':'The products of this brand are not available'}))


# Show all Categories
class CategoriesVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ProductsCategory.objects.all()
    serializer_class = serializers.CategoriesSerializer


# Show all Parent Category
class CategoryParentVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = CategoryParent.objects.all()
    serializer_class = serializers.CategoryParentSerializer


# Show all Product Tags and create new one by permission admin
class ProductsTagsVS(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ProductsTags.objects.all()
    serializer_class = serializers.ProductsTagsSerializer


    def create(self, request, *args, **kwargs):
        serializer = serializers.ProductsTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# Get a Particular product tag and update and destroy it by permission admin
class ProductsTagDetailsVS(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ProductsTags.objects.all()
    serializer_class = serializers.ProductsTagsSerializer


    def retrieve(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        tag=ProductsTags.objects.filter(pk=pk).first()
        serializer = serializers.ProductsTagsSerializer(tag)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        tag=ProductsTags.objects.filter(pk=pk).first()
        serializer = serializers.ProductsTagsSerializer(tag,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        tag=ProductsTags.objects.filter(pk=pk).first()
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Show all products
class ProductsVS(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    pagination_class = ProductListPagination

    def create(self, request, *args, **kwargs):
        serializer = serializers.ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# retrieve a Particular Product and update and destroy a Particular Product by permission admin
class ProductDetailsVS(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Products.objects.all()
    serializer_class = serializers.ProductsSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        product = Products.objects.filter(pk=pk).first()
        serializer = serializers.ProductsSerializer(product)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        brand = Products.objects.filter(pk=pk).first()
        serializer = serializers.ProductsSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        brand = Products.objects.filter(pk=pk).first()
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Show gallery products
class ProductGalleryGL(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ProductGallery.objects.all()
    serializer_class = serializers.ProductsGallerySerializer

    def create(self, request, *args, **kwargs):
        serializer = serializers.ProductsGallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# Show all Product Ratings
class ProductRatingsVS(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = UserRating.objects.all()
    serializer_class = serializers.ProductRatingsSerializer

# Show All Product Comments
class ProductCommentsGV(generics.ListAPIView):
    serializer_class = serializers.ProductsCommentSerializer
    throttle_classes = [ProductCommentsThrottle,]

    def get_queryset(self):
        product = self.kwargs['id']
        comments = ProductsComments.objects.filter(product_id=product, product__haveComments=True).all()
        if comments is None:
            return Response(serializers.ValidationError({'error':'Product comments are closed!!!'}))
        return comments

# Show a Particular Product Comment
class ProductCommentGR(generics.RetrieveAPIView):
    serializer_class = serializers.ProductsCommentSerializer

    def get_queryset(self):
        product = self.kwargs['id']
        pk = self.kwargs['pk']
        comment = ProductsComments.objects.filter(product_id=product, pk=pk).all()
        if comment is not []:
            return comment
        return Response({'error': 'Product comment are not available!!!'})


# Create Product Comment by Auth
class CreateProductCommentGC(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.CreateProductsCommentSerializer
    throttle_classes = [ProductCommentsThrottle,]

    def create(self, request, *args, **kwargs):
        serializer = serializers.CreateProductsCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# Show, update and destroy a Product Comment by owner ...
class ChangeProductCommentGRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly,]
    serializer_class = serializers.CreateProductsCommentSerializer
    throttle_classes = [ProductCommentsThrottle,]

    def retrieve(self, request, *args, **kwargs):
        product = self.kwargs['id']
        pk = self.kwargs['pk']
        comment = ProductsComments.objects.filter(product_id=product,pk=pk,user_id=request.user.id).first()
        serializer = serializers.ProductsCommentSerializer(comment)
        if serializer is None:
            return Response(serializers.ValidationError({'error': 'Product comments are closed!!!'}))
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        product_id=self.kwargs['id']
        comment = ProductsComments.objects.filter(product_id=product_id,user_id=request.user.id).first()
        serializer = serializers.CreateProductsCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        product_id = self.kwargs['id']
        comment = ProductsComments.objects.filter(product_id=product_id, user_id=request.user.id).first()
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Filter products by category
class CategoryFilteringGA(generics.ListAPIView):
    serializer_class = serializers.CategoriesSerializer
    queryset = ProductsCategory

    def get_queryset(self):
        cat_name = self.request.query_params.get('cat')
        if cat_name is not None:
            cat = ProductsCategory.objects.filter(urlTitle=cat_name)
            return cat
        else:
            return Response(serializers.ValidationError({'error': 'The products of this category are not available'}))

class ProductCommentDetailsVS(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = ProductsComments.objects.all()
    serializer_class = serializers.ProductsCommentSerializer

    def retrieve(self, request, *args, **kwargs):
        query = ProductsComments.objects.filter(product_id=self.kwargs['id'], pk=self.kwargs['pk']).first()
        serializer = serializers.ProductsCommentSerializer(query)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        query = ProductsComments.objects.filter(product_id=self.kwargs['pk'], pk=self.kwargs['pk']).first()
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Products
        fields = ['category',]


class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter