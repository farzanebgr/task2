from rest_framework.routers import DefaultRouter
from django.urls import path, include
from productionsApp.api import views

router = DefaultRouter()
router.register('product-ratings', views.ProductRatingsVS, basename='product-ratings')

urlpatterns = [
    path('', include(router.urls)),
    # Products' Links
    path('products/', views.ProductsVS.as_view(), name='all-production'),
    path('products/gallery/', views.ProductGalleryGL.as_view(), name='product-galleries'),
    path('products/<int:pk>', views.ProductDetailsVS.as_view(), name='brand-detail'),
    path('product-list/', views.ProductList.as_view(), name='product-list-by-price'),
    # Brands' Links
    path('brands/', views.BrandsVS.as_view(), name='all-brands'),
    path('brands/<int:pk>', views.BrandDetailsVS.as_view(), name='brand-detail'),
    path('brands/<brand>', views.BrandFilteringGA.as_view(), name='product-list-by-brand'),
    # Categories' Links
    path('category/', views.CategoryFilteringGA.as_view(), name='product-list-by-brand'),
    # Tags' Links
    path('tag/', views.ProductsTagsVS.as_view(), name='all-tags'),
    path('tag/<int:pk>/',views.ProductsTagDetailsVS.as_view(), name='all-tags'),
    # Product Comments
    path('<int:id>/product-comments/', views.ProductCommentsGV.as_view(), name='product-comments'),
    path('<int:id>/product-comments/<int:pk>/', views.ProductCommentGR.as_view(), name='product-comment'),
    path('<int:id>/product-comments/create/', views.CreateProductCommentGC.as_view(), name='product-comments-create'),
    path('<int:id>/product-comments/change/<int:pk>/', views.ChangeProductCommentGRUD.as_view(),
         name='product-comments-change'),
    # Brand Comments
    path('<int:id>/brand-comments/', views.BrandCommentsGL.as_view(), name='brand-comments'),
    path('<int:id>/brand-comments/<int:pk>/', views.BrandCommentGR.as_view(), name='brand-comment'),
    path('<int:id>/brand-comments/create/', views.CreateBrandCommentGC.as_view(), name='brand-comments-create'),
    path('<int:id>/brand-comments/change/<int:pk>/', views.ChangeBrandCommentGRUD.as_view(),
         name='brand-comments-change'),
]
