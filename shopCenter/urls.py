"""shopCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URLs
    path('', include('homeApp.urls')),
    path('', include('contactApp.urls')),
    path('', include('userAccountApp.urls')),
    path('userpanel/', include('userPanelApp.urls')),
    path('order/', include('orderApp.urls')),
    path('productions/', include('productionsApp.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('admin/', admin.site.urls),

    # API URLs Version 1
    path('api/v1/', include('homeApp.api.urls')),
    path('api/v1/', include('contactApp.api.urls')),
    path('api/v1/', include('userAccountApp.api.urls')),
    path('api/v1/userpanel/', include('userPanelApp.api.urls')),
    path('api/v1/order/', include('orderApp.api.urls')),
    path('api/v1/productions/', include('productionsApp.api.urls')),
    path('api/v1/ratings/', include('star_ratings.urls', namespace='ratings')),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
