from rest_framework.routers import DefaultRouter
from django.urls import path, include
from productionsApp.api.views import BrandsVS, CategoriesVS, CategoryParentVS, ProductsTagsVS, ProductsVS,\
    ProductGalleryVS, ProductCommentDetailsVS, CreateBrandsCommentsAV, BrandCommentsVS

router = DefaultRouter()
router.register('brands', BrandsVS, basename='all-brands')
router.register('categories', CategoriesVS, basename='all-categories')
router.register('category-parent', CategoryParentVS, basename='category-parent')
router.register('tags', ProductsTagsVS, basename='all-tags')
router.register('products', ProductsVS, basename='all-productions')
router.register('product-galleries', ProductGalleryVS, basename='product-galleries')
router.register('product-comments', ProductCommentDetailsVS, basename='product-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('<int:pk>/brand-comments/', BrandCommentsVS.as_view(), name='brand-comments'),
    path('<int:pk>/brand-comments/create/', CreateBrandsCommentsAV.as_view(), name='create-comment-brand'),
    # path('<int:pk>/brand-comment/<int:id>/', CreateBrandsCommentsAV.as_view(), name='brand-comment'),

]
