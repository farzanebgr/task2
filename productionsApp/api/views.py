from rest_framework import viewsets
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from productionsApp.api.permissions import IsAdminOrReadOnly, IsAdminOrIsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
from productionsApp.api.serializers import ProductsSerializer, ProductsGallerySerializer, ProductsCommentSerializer, \
    BrandsSerializer, CategoriesSerializer, CategoryParentSerializer, ProductsTagsSerializer, BrandsCommentsSerializer,\
    BrandRatingsSerializer
from productionsApp.models import ProductsBrand, BrandsComments, ProductsCategory, CategoryParent, ProductsTags, \
    Products, ProductsComments, ProductGallery
from star_ratings.models import UserRating


# Show all Brands
class BrandsVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ProductsBrand.objects.all()
    serializer_class = BrandsSerializer

# Show all Brands
class BrandRatingsVS(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = UserRating.objects.all()
    serializer_class = BrandRatingsSerializer


# Show  Brand Comments
class BrandCommentsVS(generics.ListAPIView):
    serializer_class = BrandsCommentsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        comments = BrandsComments.objects.filter(brand_id=pk, brand__haveComments=True).all()
        return comments


# Create Comment for brand
class CreateBrandsCommentsAV(mixins.CreateModelMixin,
                             generics.GenericAPIView):
    serializer_class = BrandsCommentsSerializer
    queryset = BrandsComments.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        brand = BrandsComments.objects.filter(brand_id=pk)
        user_info = request.user
        user = BrandsComments.objects.filter(user_id=user_info.id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(brand=brand, user=user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


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
class ProductCommentVS(generics.ListAPIView):
    serializer_class = ProductsCommentSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        comments = ProductsComments.objects.filter(product_id=pk, product__haveComments=True).all()
        return comments


class ProductCommentDetailsVS(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = ProductsComments.objects.all()
    serializer_class = ProductsCommentSerializer

    def retrieve(self, request, *args, **kwargs):
        query = ProductsComments.objects.filter(product_id=self.kwargs['pk'], pk=self.kwargs['pk']).first()
        serializer = ProductsCommentSerializer(query)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        query = ProductsComments.objects.filter(product_id=self.kwargs['pk'], pk=self.kwargs['pk']).first()
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
