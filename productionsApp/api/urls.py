from rest_framework.routers import DefaultRouter
from django.urls import path, include
from productionsApp.api.views import BrandsVS, CategoriesVS, CategoryParentVS, ProductsTagsVS, ProductsVS,\
    ProductGalleryVS, ProductCommentDetailsVS, CategoryFilteringGA, BrandCommentsVS, ProductCommentVS,\
    ProductRatingsVS, BrandFilteringGA, ProductList, BrandDetailsVS, ProductDetailsVS

router = DefaultRouter()
# router.register('products', ProductsVS, basename='all-productions')
router.register('product-ratings', ProductRatingsVS, basename='product-ratings')
#add product comment
#add brand comment
router.register('category', CategoriesVS, basename='all-categories')
router.register('category-parent', CategoryParentVS, basename='category-parent')
router.register('tags', ProductsTagsVS, basename='all-tags')
router.register('product-galleries', ProductGalleryVS, basename='product-galleries')
router.register('product-comment-details', ProductCommentDetailsVS, basename='product-comment-details')


urlpatterns = [
    path('', include(router.urls)),

    path('products/', ProductsVS.as_view(), name='all-production'),
    path('products/<int:pk>', ProductDetailsVS.as_view(), name='brand-detail'),

    path('brands/', BrandsVS.as_view(), name='all-brands'),
    path('brands/<int:pk>', BrandDetailsVS.as_view(), name='brand-detail'),
    path('brands/<brand>', BrandFilteringGA.as_view(), name='product-list-by-brand'),

    path('category/', CategoryFilteringGA.as_view(), name='product-list-by-brand'),

    path('product-list/', ProductList.as_view(), name='product-list-by-price'),

    path('<int:pk>/', include(router.urls)),
    path('<int:pk>/brand-comments/', BrandCommentsVS.as_view(), name='brand-comments'),
    path('<int:id>/product-comments/', ProductCommentVS.as_view(), name='product-comments'),
]
