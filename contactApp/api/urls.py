# Import from rest_framework. something
from rest_framework.routers import DefaultRouter
# Import from django. something for url
from django.urls import path, include
# Import APIViews from app folder
from contactApp.api.views import CopyRightAV, ContactUsVS

# Routing for APIView
router = DefaultRouter()
router.register('contact-us', ContactUsVS, basename='contact-us')

urlpatterns = [
    path('', include(router.urls)),
    path('copy-right/', CopyRightAV.as_view(), name='copy-right'),
]
