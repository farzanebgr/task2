from django.urls import path
from productionsApp import views

urlpatterns = [
    path('', views.AllProductionsView.as_view(), name='all-productions-page'),
    path('<slug:slug>/', views.ProductionsDetailView.as_view(), name='detail-productions-page'),
    path('add-product-comment/', views.addProductComment, name='product-comment-page'),
    path('add-brand-comment/', views.addBrandComment, name='brand-comment-page'),
    path('brands/', views.BrandsListView.as_view(), name='brands-page'),
    path('brands/<brand>', views.AllProductionsView.as_view(), name='product-list-by-brand'),
    path('category/<cat>', views.AllProductionsView.as_view(), name='product-list-by-category'),
    path('<pk>/', views.BrandDetailView.as_view(), name='brand-detail-page'),
]
