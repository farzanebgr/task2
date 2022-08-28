from rest_framework.routers import DefaultRouter
from django.urls import path, include
from homeApp.api import views

router = DefaultRouter()
router.register('slider', views.IndexSliderDetailsVS, basename='slider')
router.register('latest-products', views.LatestProductsDetailsVS, basename='latest-products')
router.register('most-visit-products', views.MostVisitProductsDetailsVS, basename='most-visit-products')
router.register('about-us', views.AboutUsDetailsVS, basename='about-us')
router.register('site-header', views.SiteHeaderPartialVS, basename='site-header')
router.register('site-footer', views.SiteFooterPartialVS, basename='site-footer')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
]
