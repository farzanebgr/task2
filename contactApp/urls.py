from django.urls import path
from . import views

urlpatterns = [
    path('contact-us/', views.contactUsView.as_view(), name='contact-us-page'),
    path('sendMessage', views.contactUsView.as_view(), name='send-message'),
    path('copy-right/', views.contactUsView.as_view(), name='copy-right-page'),

]
