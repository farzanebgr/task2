from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from siteSettingsApp.models import settingModel
from .forms import contactUsModelForm
from django.views.generic.edit import CreateView
from userAccountApp.models import User

from .models import contactUs


class contactUsView(CreateView):
    form_class = contactUsModelForm
    template_name = 'contactApp/contactUs.html'
    success_url = '/contact-us-page/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['settings'] = settings
        return context

    def post(self, request):
        contactUs_form = contactUsModelForm(request.POST)
        if contactUs_form.is_valid():
            user_email = contactUs_form.cleaned_data.get('email')
            user_title = contactUs_form.cleaned_data.get('title')
            user_fullName = contactUs_form.cleaned_data.get('fullName')
            user_message = contactUs_form.cleaned_data.get('message')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if not user:
                contactUs_form.add_error('email', 'شما هنوز وارد سایت نشده اید')
                pm = 'متاسفانه شما در سایت ثبت نام نکرده اید. برای ثبت نظر خود باید ابتدا وارد حساب کاربری شوید.'
                settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
                context = {
                    'pm': pm,
                    'settings': settings
                }

                return render(request, 'contactApp/showMessages.html', context)
            else:
                message = contactUs(
                    email=user_email,
                    title=user_title,
                    fullName=user_fullName,
                    message=user_message,
                )
                message.save()
                settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
                sendit = 'پیام شما با موفقیت ارسال شد. مدیران سایت برای پاسخگویی جواب را به ایمیل ' \
                         'شما ارسال می کنند. '
                context = {
                    'sendit': sendit,
                    'settings': settings
                }
                return render(request, 'contactApp/showMessages.html', context)

        context = {
            'register_form': contactUs_form
        }

        return render(request, 'contactApp/contactUs.html', context)


class copyrightView(TemplateView):
    template_name = 'contactApp/copyRight.html'
    success_url = '/copy-right-page/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        settings: settingModel = settingModel.objects.filter(isMainSettings=True).first()
        context['settings'] = settings
        return context