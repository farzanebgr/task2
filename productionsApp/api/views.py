from rest_framework import viewsets
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from productionsApp.api.permissions import IsAdminOrReadOnly, IsAdminOrIsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
from productionsApp.api.serializers import ProductsSerializer, ProductsGallerySerializer, ProductsCommentSerializer, \
    BrandsSerializer, CategoriesSerializer, CategoryParentSerializer, ProductsTagsSerializer, BrandsCommentsSerializer
from productionsApp.models import ProductsBrand, BrandsComments, ProductsCategory, CategoryParent, ProductsTags, \
    Products, ProductsComments, ProductGallery
from django.core.exceptions import ValidationError


# Show all Brands
class BrandsVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ProductsBrand.objects.all()
    serializer_class = BrandsSerializer


# Show  Brand Comments
class BrandCommentsVS(generics.ListAPIView):
    serializer_class = BrandsCommentsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        comments = BrandsComments.objects.filter(brand_id=pk)
        return comments


# Create Comment for brand
class CreateBrandsCommentsAV(mixins.CreateModelMixin,
                             generics.CreateAPIView):
    serializer_class = BrandsCommentsSerializer
    queryset = BrandsComments.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return None


# Show all Categories
class CategoriesVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ProductsCategory.objects.all()
    serializer_class = CategoriesSerializer


# Show all Parent Category
class CategoryParentVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = CategoryParent.objects.all()
    serializer_class = CategoryParentSerializer


# Show all Tags Products
class ProductsTagsVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ProductsTags.objects.all()
    serializer_class = ProductsTagsSerializer


# Show all products
class ProductsVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


# Show gallery products
class ProductGalleryVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ProductGallery.objects.all()
    serializer_class = ProductsGallerySerializer


# Show Comment Product
class ProductCommentDetailsVS(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = ProductsComments.objects.all()
    serializer_class = ProductsCommentSerializer

    def list(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.user:
                serializer = ProductsCommentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
            else:
                return Response(serializers.ValidationError({'error': 'you are not login into site!'}))

        if request.method == 'GET':
            query = ProductsComments.objects.filter(product_id=self.kwargs['pk']).all()
            serializer = ProductsCommentSerializer(query, many=True)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        query = ProductsComments.objects.filter(product_id=self.kwargs['pk'], pk=self.kwargs['pk']).first()
        serializer = ProductsCommentSerializer(query)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        query = ProductsComments.objects.filter(product_id=self.kwargs['pk'], pk=self.kwargs['pk']).first()
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
