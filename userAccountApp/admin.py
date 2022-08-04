from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_filter = ['is_active', 'is_superuser']
    list_display = ['username', 'email',  'last_login', 'date_joined', 'is_active']


admin.site.register(User, UserAdmin)
