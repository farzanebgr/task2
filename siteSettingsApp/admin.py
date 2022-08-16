from django.contrib import admin

from siteSettingsApp.models import settingModel, footerLinkBox, footerLink, Slider


class siteSettingModel(admin.ModelAdmin):
    list_filter = ['siteEnglishName']
    list_display = ['siteName', 'siteAddress', 'siteEmail', 'siteLogo', 'isMainSettings']


class footerLinkBoxModel(admin.ModelAdmin):
    list_display = ['title', 'titleEnglish']


class footerLinkModel(admin.ModelAdmin):
    list_filter = ['titleEnglish']
    list_display = ['title', 'titleEnglish', 'footerLinkRelation', 'url']


class sliderModel(admin.ModelAdmin):
    list_filter = ['isActive', 'title']
    list_display = ['title', 'titleEN', 'url_title', 'image', 'isActive']


admin.site.register(settingModel, siteSettingModel)
admin.site.register(footerLinkBox, footerLinkBoxModel)
admin.site.register(footerLink, footerLinkModel)
admin.site.register(Slider, sliderModel)
