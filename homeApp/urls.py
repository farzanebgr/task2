from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView.as_view(), name='index-page'),
    path('about-us/', views.aboutUsView.as_view(), name='about-us-page'),

]
