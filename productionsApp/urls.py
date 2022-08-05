from django.urls import path
from productionsApp import views

urlpatterns = [
    path('', views.AllProductionsView.as_view(), name='all-productions-page'),
    path('<slug:slug>', views.DetailsProductionsView.as_view(), name='detail-productions-page'),
    path('categories/', views.CategoriesProductionsView.as_view(), name='categories-productions-page'),
    path('categories/<str:category>', views.CategoriesProductionsView.as_view(), name='filter-by-categories-productions'),

]
