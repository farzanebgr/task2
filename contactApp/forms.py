from django import forms

from .models import contactUs


class contactUsModelForm(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = ['title', 'email', 'fullName', 'message']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fullName': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message'
            })
        }
        labels = {
            'title': 'موضوع پیام شما',
            'email': 'آدرس ایمیل شما',
            'fullName': 'نام و نام خانوادگی شما',
            'message': 'متن پیام شما'
        }
        error_messages = {
            'fullName': {
                'required': 'نام و نام خانوادگی شما نیاز است. لطفا نام و نام خانوادگی خود را وارد کنید'
            }
        }
