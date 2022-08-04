from django.contrib.auth import login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from userAccountApp.froms import registerForm, loginForm
from userAccountApp.models import User


class registerView(View):
    def get(self, request):
        register_form = registerForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'userAccountApp/registerPage.html', context)

    def post(self, request):
        register_form = registerForm(request.POST)
        login_form = loginForm(request.POST)
        if register_form.is_valid():
            user_username = register_form.cleaned_data.get('username')
            user_firstname = register_form.cleaned_data.get('first_name')
            user_lastname = register_form.cleaned_data.get('last_name')
            user_age = register_form.cleaned_data.get('age')
            user_mobile = register_form.cleaned_data.get('mobile')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    username=user_username,
                    first_name=user_firstname,
                    last_name=user_lastname,
                    age=user_age,
                    mobile=user_mobile,
                    is_active=True, )
                new_user.set_password(user_password)
                new_user.save()
                message = 'در سایت ثبت نام شدید. برای ورود به پنل کاربری اطلاعات خواسته شده را وارد کنید.'
        context = {
            'login_form': login_form,
            'showMessage': message
        }

        return render(request, 'userAccountApp/loginPage.html', context)


class loginView(View):
    def get(self, request):
        login_form = loginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'userAccountApp/loginPage.html', context)

    def post(self, request: HttpRequest):
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('index-page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'userAccountApp/loginPage.html', context)


class logoutView(View):
        def get(self, request):
            logout(request)
            message = 'از حساب کاربری خود خارج شدید. برای ورود مجدد از طریق لینک زیر اقدام کنید.'
            context = {
                'showMessage': message
                      }
            return render(request, 'userAccountApp/logoutPage.html', context)
