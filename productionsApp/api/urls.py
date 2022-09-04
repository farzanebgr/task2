from rest_framework.routers import DefaultRouter
from django.urls import path, include
from productionsApp.api.views import BrandsVS, CategoriesVS, CategoryParentVS, ProductsTagsVS, ProductsVS,\
    ProductGalleryGL, ProductCommentDetailsVS, CategoryFilteringGA, BrandCommentsVS, ProductCommentGV,\
    ProductRatingsVS, BrandFilteringGA, ProductList, BrandDetailsVS, ProductDetailsVS,CreateProductCommentGC

router = DefaultRouter()
router.register('product-ratings', ProductRatingsVS, basename='product-ratings')

router.register('category', CategoriesVS, basename='all-categories')
router.register('category-parent', CategoryParentVS, basename='category-parent')
router.register('tags', ProductsTagsVS, basename='all-tags')
router.register('product-comment-details', ProductCommentDetailsVS, basename='product-comment-details')


urlpatterns = [
    #add product comment
    #add brand comment
    path('', include(router.urls)),
    # Products' Links
    path('products/', ProductsVS.as_view(), name='all-production'),
    path('products/gallery/', ProductGalleryGL.as_view(), name='product-galleries'),
    path('products/<int:pk>', ProductDetailsVS.as_view(), name='brand-detail'),
    path('product-list/', ProductList.as_view(), name='product-list-by-price'),
    # Brands' Links
    path('brands/', BrandsVS.as_view(), name='all-brands'),
    path('brands/<int:pk>', BrandDetailsVS.as_view(), name='brand-detail'),
    path('brands/<brand>', BrandFilteringGA.as_view(), name='product-list-by-brand'),
    # Categories' Links
    path('category/', CategoryFilteringGA.as_view(), name='product-list-by-brand'),


    path('<int:pk>/', include(router.urls)),
    path('<int:pk>/brand-comments/', BrandCommentsVS.as_view(), name='brand-comments'),
    path('<int:id>/product-comments/', ProductCommentGV.as_view(), name='product-comments'),
    path('<int:id>/product-comments/create/', CreateProductCommentGC.as_view(), name='product-comments-create'),
]
