from rest_framework.routers import DefaultRouter

from django.urls import path, include
from productionsApp.api.views import ProductsVS, ProductGalleryVS, ProductsCommentsVS

router = DefaultRouter()
router.register('products', ProductsVS, basename='all-products')
router.register('product-galleries', ProductGalleryVS, basename='product-galleries')
router.register('product-comment', ProductsCommentsVS, basename='product-comments')

urlpatterns = [
    path('', include(router.urls)),
    # path('comment-create/', ProductCommentCreateVS.as_view(), name='comment-create'),
    # path('', views.ProductsDetailVS.as_view(), name='all-productions'),
    # path('<slug:slug>', views.ProductionsDetailView.as_view(), name='detail-productions-page'),
    # path('add-product-comment/', views.addProductComment, name='product-comment-page'),
    # path('categories/', views.CategoriesProductionsView.as_view(), name='categories-productions-page'),
    # path('add-brand-comment/', views.addBrandComment, name='brand-comment-page'),
    # path('brands/', views.BrandsListView.as_view(), name='brands-page'),
    # path('brands/<brand>', views.AllProductionsView.as_view(), name='product-list-by-brand'),
    # path('category/<cat>', views.AllProductionsView.as_view(), name='product-list-by-category'),
    # path('new-brands/', views.newBrandsListView.as_view(), name='new-brands-page'),
    # path('<pk>/', views.BrandDetailView.as_view(), name='brand-detail-page'),
    # path('categories/<str:category>', views.CategoriesProductionsView.as_view(), name='filter-by-categories-productions')
]