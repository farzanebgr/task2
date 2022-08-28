from django.urls import path
from homeApp.api import views

urlpatterns = [
    path('', views.indexView.as_view(), name='index-page'),
    path('slider/', views.IndexSliderAV.as_view(), name='slider'),
    path('slider/<int:pk>/', views.IndexSliderDetailsAV.as_view(), name='slider-details'),
    path('about-us/', views.aboutUsView.as_view(), name='about-us-page'),

]
