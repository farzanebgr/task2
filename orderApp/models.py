from django.db import models
from userAccountApp.models import User
from productionsApp.models import Products


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    isPaid = models.BooleanField(verbose_name='نهایی شده/ نشده')
    paymentDate = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = ' سبد های خرید کاربران'

    def calculate_total_price(self):
        total_amount = 0
        if self.isPaid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.finalPrice * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count

        return total_amount

    def __str__(self):
        return str(self.user)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصول')
    finalPrice = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'جزئیات سبد خرید'
        verbose_name_plural = 'لیست جزئیات سبد های خرید'

    def __str__(self):
        return str(self.order)

    def get_total_price(self):
        return self.count * self.product.price
