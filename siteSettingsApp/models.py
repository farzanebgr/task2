from django.db import models


class settingModel(models.Model):
    siteName = models.CharField(max_length=200, verbose_name='نام سایت')
    siteEnglishName = models.CharField(max_length=200, verbose_name='نام انگلیسی سایت')
    siteUrl = models.CharField(max_length=200, verbose_name='دامنه سایت')
    siteAddress = models.CharField(max_length=200, verbose_name='آدرس سایت')
    sitePhone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن سایت')
    siteFax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس سایت')
    siteEmail = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل سایت')
    siteCopyRight = models.CharField(max_length=200, verbose_name='متن کپی رایت سایت')
    siteRights = models.TextField(verbose_name='متن کپی رایت سایت', null=True, blank=True)
    siteLogo = models.ImageField(upload_to='uploads/images/siteSettings', verbose_name='لوگو سایت')
    siteMap = models.ImageField(upload_to='uploads/images/siteSettings', verbose_name='نقشه سایت')
    siteAboutUs = models.TextField(verbose_name='درباره ما')
    isMainSettings = models.BooleanField(verbose_name='تنظیمات اصلی')

    def __str__(self):
        return self.siteName

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنطیمات'


class footerLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام دسته لینک')
    titleEnglish = models.CharField(max_length=200, verbose_name='نام انگلیسی دسته لینک', null=True)

    class Meta:
        verbose_name = 'دسته بندی آدرس ها در فوتر'
        verbose_name_plural = 'دسته بندی های آدرس ها در فوتر'

    def __str__(self):
        return self.title


class footerLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    titleEnglish = models.CharField(max_length=200, verbose_name='نمایش متن کمکی')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footerLinkRelation = models.ForeignKey(to=footerLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی',
                                           related_name='footerLinkRelation')

    class Meta:
        verbose_name = 'آدرس در فوتر'
        verbose_name_plural = 'آدرس ها در فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    titleEN = models.CharField(max_length=200, verbose_name='عنوان انگلیسی')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/sliders/', verbose_name='تصویر اسلایدر')
    isActive = models.BooleanField(verbose_name='فعال بودن /نبودن')

    class Meta:
        verbose_name = ' اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title
