from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(verbose_name='شماره تلفن همراه', max_length=20, null=True, blank=True)
    age = models.IntegerField(verbose_name='سن کاربر', null=True, blank=True)
    avatar = models.ImageField(upload_to='user/', verbose_name='تصویر نمایه کاربر', null=True, blank=True)
    aboutUser = models.TextField(verbose_name='درباره کاربر', null=True, blank=True, )
    address = models.TextField(null=True, blank=True, verbose_name='آدرس کاربر')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
