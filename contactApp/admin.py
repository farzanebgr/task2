from django.contrib import admin
from contactApp.models import contactUs

# Show contact us model in admin panel With customization
class contactUsModel(admin.ModelAdmin):
    list_filter = ['isReadByAdmin', 'createdDate']
    list_display = ['fullName', 'title', 'email', 'isReadByAdmin']


# Register contact us model in admin panel
admin.site.register(contactUs, contactUsModel)
