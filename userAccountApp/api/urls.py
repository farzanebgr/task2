from django.urls import path

from userAccountApp.api.views import registration_view
urlpatterns = [
    path('register/', registration_view, name='register'),
]