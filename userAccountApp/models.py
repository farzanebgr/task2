from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(verbose_name='شماره تلفن همراه', max_length=20)
    age = models.IntegerField(verbose_name='سن کاربر', null=True, blank=True)
    avatar = models.ImageField(upload_to='user/', verbose_name='تصویر نمایه کاربر', null=True, blank=True)
    aboutUser = models.TextField(verbose_name='درباره کاربر',null=True, blank=True,)
    address = models.TextField(null=True, blank=True, verbose_name='آدرس کاربر')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
