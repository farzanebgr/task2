from rest_framework.routers import DefaultRouter
from django.urls import path, include
from contactApp.api.views import CopyRightAV, ContactUsVS


router = DefaultRouter()
router.register('contact-us', ContactUsVS, basename='contact-us')
urlpatterns = [
    path('', include(router.urls)),
    # path('send-message/', ContactUsView.as_view(), name='send-message'),
    path('copy-right/', CopyRightAV.as_view(), name='copy-right'),
]
