from django.contrib import admin
from .models import contactUs


class contactUsModel(admin.ModelAdmin):
    list_filter = ['isReadByAdmin', 'createdDate']
    list_display = ['fullName', 'title', 'email', 'isReadByAdmin']


admin.site.register(contactUs, contactUsModel)
