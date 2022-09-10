# Import from django. something
from django.urls import path
# Import views file to get views for urls
from homeApp.views import indexView, aboutUsView

urlpatterns = [
    path('', indexView.as_view(), name='index-page'),
    path('about-us/', aboutUsView.as_view(), name='about-us-page'),
]
