from django.urls import path
from contactApp.views import ContactUsView, CopyRightView
urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('send-message/', ContactUsView.as_view(), name='send-message'),
    path('copy-right/', CopyRightView.as_view(), name='copy-right'),
]
