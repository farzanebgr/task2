from django.contrib.auth import get_user_model
from django.db import models


# from userAccountApp.models import User
from shopCenter import settings

# Contact us's Fields in database by verbose name and some settings
class contactUs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usercontact')
    fullName = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    email = models.CharField(max_length=300, verbose_name='آدرس ایمیل')
    title = models.CharField(max_length=300, verbose_name='عنوان پیام')
    message = models.TextField(verbose_name='متن پیام تماس با ما')
    createdDate = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
    isReadByAdmin = models.BooleanField(verbose_name='خوانده شده توسط مدیر', default=False)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title
