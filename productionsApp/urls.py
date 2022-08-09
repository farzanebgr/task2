from django.urls import path
from productionsApp import views

urlpatterns = [
    path('', views.AllProductionsView.as_view(), name='all-productions-page'),
    path('<slug:slug>', views.ProductionsDetailView.as_view(), name='detail-productions-page'),
    path('add-product-comment/', views.addProductComment, name='product-comment-page'),
    path('categories/', views.CategoriesProductionsView.as_view(), name='categories-productions-page'),
    path('brands/', views.BrandsListView.as_view(), name='brands-page'),
    path('<pk>/', views.BrandDetailView.as_view(), name='brand-detail-page'),
    path('categories/<str:category>', views.CategoriesProductionsView.as_view(), name='filter-by-categories-productions')
]
