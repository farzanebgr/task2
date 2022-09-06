from django import forms
from contactApp.models import contactUs


# Create a model form for contact us information that user send to database
class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = contactUs
        # Necessary fields from contact us model in database
        fields = ['title', 'email', 'fullName', 'message']
        # Some settings like input types for fields and give attributes such as id and class to style
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
        # Label the fields to display to the user
        labels = {
            'title': 'موضوع پیام شما',
            'email': 'آدرس ایمیل شما',
            'fullName': 'نام و نام خانوادگی شما',
            'message': 'متن پیام شما'
        }
        # If an error occurs, it will give an error message to the user for each field
        error_messages = {
            'fullName': {
                'required': 'نام و نام خانوادگی شما نیاز است. لطفا نام و نام خانوادگی خود را وارد کنید'
            }
        }
