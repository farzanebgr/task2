from rest_framework.routers import DefaultRouter
from django.urls import path, include
from productionsApp.api.views import BrandsVS, CategoriesVS, CategoryParentVS, ProductsTagsVS, ProductsVS,\
    ProductGalleryGL, ProductCommentDetailsVS, CategoryFilteringGA, BrandCommentsGL, ProductCommentGR,\
    ProductRatingsVS, BrandFilteringGA, ProductList, BrandDetailsVS, ProductDetailsVS,CreateProductCommentGC,\
    ChangeProductCommentGRUD, ProductCommentsGV, BrandCommentGR, CreateBrandCommentGC, ChangeBrandCommentGRUD

router = DefaultRouter()
router.register('product-ratings', ProductRatingsVS, basename='product-ratings')

router.register('category', CategoriesVS, basename='all-categories')
router.register('category-parent', CategoryParentVS, basename='category-parent')
router.register('tags', ProductsTagsVS, basename='all-tags')
router.register('product-comment-details', ProductCommentDetailsVS, basename='product-comment-details')


urlpatterns = [
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
    # Product Comments
    path('<int:id>/product-comments/', ProductCommentsGV.as_view(), name='product-comments'),
    path('<int:id>/product-comments/<int:pk>/', ProductCommentGR.as_view(), name='product-comment'),
    path('<int:id>/product-comments/create/', CreateProductCommentGC.as_view(), name='product-comments-create'),
    path('<int:id>/product-comments/change/<int:pk>/', ChangeProductCommentGRUD.as_view(),
         name='product-comments-change'),
    # Brand Comments
    path('<int:id>/brand-comments/', BrandCommentsGL.as_view(), name='brand-comments'),
    path('<int:id>/brand-comments/<int:pk>/', BrandCommentGR.as_view(), name='brand-comment'),
    path('<int:id>/brand-comments/create/', CreateBrandCommentGC.as_view(), name='brand-comments-create'),
    path('<int:id>/brand-comments/change/<int:pk>/', ChangeBrandCommentGRUD.as_view(),
         name='brand-comments-change'),
]
