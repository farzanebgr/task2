from django.db import models
from django.shortcuts import reverse
from jalali_date import datetime2jalali, date2jalali
from userAccountApp.models import User


class ProductsCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان دسته بندی')
    urlTitle = models.CharField(max_length=300, db_index=True, verbose_name='Url عنوان در')
    image = models.ImageField(upload_to='images/category', null=True, blank=True, verbose_name='تصویر دسته بندی')
    isActive = models.BooleanField(verbose_name='فعال / غیرفعال')
    isDelete = models.BooleanField(verbose_name='حذف شده / نشده', null=True)
    parent = models.ForeignKey('CategoryParent', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی  های محصولات'


class CategoryParent(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='نام')
    titleEN = models.CharField(max_length=300, db_index=True, verbose_name='نام انگلیسی', null=True)
    isActive = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'دسته بندی والد'
        verbose_name_plural = 'دسته بندی های والد'

    def __str__(self):
        return self.title


class ProductsBrand(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='نام برند')
    titleEN = models.CharField(max_length=300, db_index=True, verbose_name='نام انگلیسی برند', null=True)
    isActive = models.BooleanField(verbose_name='فعال / غیرفعال')
    image = models.ImageField(upload_to='brands/', null=True, blank=True, verbose_name='تصویر محصول')
    shortDescription = models.TextField(verbose_name='توضیحات کوتاه', null=True)
    description = models.TextField(verbose_name='توضیحات برند', null=True)
    createDate = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ نوشته')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def createJalalidate(self):
        date = date2jalali(self.createDate).strftime('14%y/%m/%d')
        return date

    def createJalalitime(self):
        time = datetime2jalali(self.createDate).strftime('%H : %M')
        return time

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(ProductsCategory, related_name='productCategories',
                                      verbose_name='دسته بندی محصول')
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductsBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    numbers = models.IntegerField(verbose_name='تعداد', null=True, blank=True)
    dateOfCreate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ثبت')
    shortDescription = models.CharField(max_length=360, db_index=True, default='empty', verbose_name='توضیحات کوتاه')
    Description = models.TextField(db_index=True, verbose_name='توضیحات اصلی')
    isActive = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    isDelete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-details-page', args=[self.slug])

    def save(self, *args, **keyargs):
        super().save(*args, **keyargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductsTags(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='تگ محصول')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'


class ProductsComments(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصول')
    parent = models.ForeignKey('ProductsComments', null=True, blank=True, on_delete=models.CASCADE, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', )
    createDate = models.DateTimeField(verbose_name='تاریخ ثبت', auto_now_add=True)
    message = models.TextField(verbose_name='متن نظر')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def createJalalidate(self):
        date = date2jalali(self.createDate).strftime('14%y/%m/%d')
        return date

    def createJalalitime(self):
        time = datetime2jalali(self.createDate).strftime('%H:%M')
        return time

    def __str__(self):
        return str(self.user)
