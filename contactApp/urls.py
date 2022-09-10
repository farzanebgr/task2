# Import from django. something
from django.urls import path
# Import views for urls
from contactApp import views

urlpatterns = [
    path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
    path('send-message/', views.ContactUsView.as_view(), name='send-message'),
    path('copy-right/', views.CopyRightView.as_view(), name='copy-right'),
]
