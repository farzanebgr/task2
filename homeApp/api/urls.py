from rest_framework.routers import DefaultRouter
from django.urls import path, include
from homeApp.api import views

router = DefaultRouter()
router.register('slider', views.IndexSliderDetailsAV, basename='slider')
router.register('latest-products', views.LatestProductsDetailsAV, basename='latest-products')
router.register('most-visit-products', views.MostVisitProductsDetailsAV, basename='most-visit-products')
router.register('about-us', views.AboutUsDetailsAV, basename='about-us')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
]
