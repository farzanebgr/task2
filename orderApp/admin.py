from django.contrib import admin
from .models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['isPaid']
    list_display = ['user', 'paymentDate', 'isPaid']


class OrderDetailAdmin(admin.ModelAdmin):
    list_filter = ['order']
    list_display = ['order', 'product', 'finalPrice', 'count']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
