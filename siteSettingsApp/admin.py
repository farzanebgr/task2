from django.contrib import admin

from siteSettingsApp.models import settingModel, footerLinkBox, footerLink


class siteSettingModel(admin.ModelAdmin):
    list_filter = ['siteEnglishName']
    list_display = ['siteName', 'siteAddress', 'siteEmail', 'siteLogo', 'isMainSettings']


class footerLinkBoxModel(admin.ModelAdmin):
    list_display = ['title', 'titleEnglish']


class footerLinkModel(admin.ModelAdmin):
    list_filter = ['titleEnglish']
    list_display = ['title','titleEnglish', 'footerLinkRelation', 'url']


admin.site.register(settingModel, siteSettingModel)
admin.site.register(footerLinkBox, footerLinkBoxModel)
admin.site.register(footerLink, footerLinkModel)
