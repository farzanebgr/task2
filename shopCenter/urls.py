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
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
