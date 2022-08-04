from django.contrib import admin
from .models import Products, ProductsCategory, ProductsBrand, ProductsTags, CategoryParent


class ProductsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'price', 'slug', 'shortDescription', 'numbers', 'slug']


class BrandsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'titleEN', 'isActive']


class TagsAdmin(admin.ModelAdmin):
    list_display = ['product', 'caption']


class CategoriesAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'urlTitle', 'image', 'isActive']


class CategoryParentAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'titleEN', 'isActive']


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductsCategory, CategoriesAdmin)
admin.site.register(ProductsTags, TagsAdmin)
admin.site.register(ProductsBrand, BrandsAdmin)
admin.site.register(CategoryParent, BrandsAdmin)
