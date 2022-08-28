from django.urls import path
from homeApp.api import views

urlpatterns = [
    path('slider/', views.IndexSliderAV.as_view(), name='slider'),
    path('slider/<int:pk>/', views.IndexSliderDetailsAV.as_view(), name='slider-details'),
    path('latest-products/', views.LatestProductsAv.as_view(), name='latest-products'),
    path('latest-products/<int:pk>/', views.LatestProductsDetailsAV.as_view(), name='latest-products-details'),
    path('most-visit-products/', views.MostVisitProductsAV.as_view(), name='most-visit-products'),
    path('most-visit-products/<int:pk>/', views.MostVisitProductsDetailsAV.as_view(), name='most-visit-products-details'),
    path('about-us/', views.AboutUsAV.as_view(), name='about-us'),
    path('about-us/<int:pk>/', views.AboutUsDetailsAV.as_view(), name='about-us-details'),
]
