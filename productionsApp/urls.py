from django.urls import path
from productionsApp import views

urlpatterns = [
    path('', views.AllProductionsView.as_view(), name='all-productions-page'),
    path('<slug:slug>', views.ProductionsDetailView.as_view(), name='detail-productions-page'),
    path('add-product-comment/', views.addProductComment, name='product-comment-page'),
    path('categories/', views.CategoriesProductionsView.as_view(), name='categories-productions-page'),
    path('add-brand-comment/', views.addBrandComment, name='brand-comment-page'),
    path('brands/', views.BrandsListView.as_view(), name='brands-page'),
    path('brands/<brand>', views.AllProductionsView.as_view(), name='product-list-by-brand'),
    path('category/<cat>', views.AllProductionsView.as_view(), name='product-list-by-category'),
    path('new-brands/', views.newBrandsListView.as_view(), name='new-brands-page'),
    path('<pk>/', views.BrandDetailView.as_view(), name='brand-detail-page'),
    path('categories/<str:category>', views.CategoriesProductionsView.as_view(), name='filter-by-categories-productions')
]
