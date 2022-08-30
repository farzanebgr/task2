from rest_framework.routers import DefaultRouter
from django.urls import path, include
from productionsApp.api.views import BrandsVS, CategoriesVS, ProductsVS, ProductGalleryVS, ProductCommentDetailsVS

router = DefaultRouter()
router.register('brands', BrandsVS, basename='all-brands')
router.register('categories', CategoriesVS, basename='all-categories')
router.register('products', ProductsVS, basename='all-productions')
router.register('product-galleries', ProductGalleryVS, basename='product-galleries')
router.register('product-comments', ProductCommentDetailsVS, basename='product-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    ]
