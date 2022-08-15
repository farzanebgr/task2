from django.contrib import admin
from .models import Products, ProductsCategory, ProductsBrand, ProductsTags, CategoryParent, ProductsComments, \
    BrandsComments, ProductsVisit


class ProductsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'price', 'slug', 'shortDescription', 'productCount', 'slug']


class ProductsCommentsAdmin(admin.ModelAdmin):
    list_filter = ['product']
    list_display = ['user', 'product', 'parent', 'message', 'createDate']


class BrandsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'titleEN', 'isActive']


class BrandsCommentsAdmin(admin.ModelAdmin):
    list_filter = ['brand']
    list_display = ['user', 'brand', 'parent', 'message', 'createDate']


class TagsAdmin(admin.ModelAdmin):
    list_display = ['product', 'caption']


class CategoriesAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'urlTitle', 'image', 'isActive']


class CategoryParentAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'titleEN', 'isActive']


class ProductsVisitAdmin(admin.ModelAdmin):
    list_filter = ['product']
    list_display = ['product', 'ip', 'user']


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductsComments, ProductsCommentsAdmin)
admin.site.register(ProductsBrand, BrandsAdmin)
admin.site.register(BrandsComments, BrandsCommentsAdmin)
admin.site.register(ProductsCategory, CategoriesAdmin)
admin.site.register(ProductsTags, TagsAdmin)
admin.site.register(CategoryParent, BrandsAdmin)
admin.site.register(ProductsVisit, ProductsVisitAdmin)
