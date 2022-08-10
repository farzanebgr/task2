from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from userAccountApp.models import User
from .forms import editProfileModelForm, changePasswordForm
from django.contrib.auth import logout


class userPanelDashboard(TemplateView):
    template_name = 'userPanelApp/userPanelDashboard.html'


class editProdileView(View):

    def get(self, request: HttpRequest):
        currentUser = User.objects.filter(id=request.user.id).first()
        editForm = editProfileModelForm(instance=currentUser)
        context = {
            'form': editForm,
            'currentUser': currentUser
        }
        return render(request, 'userPanelApp/editProfile.html', context)

    def post(self, request: HttpRequest):
        currentUser = User.objects.filter(id=request.user.id).first()
        editForm = editProfileModelForm(request.POST, request.FILES, instance=currentUser)
        if editForm.is_valid():
            editForm.save(commit=True)
            context = {
                'form': editForm,
                'currentUser': currentUser
            }
        return render(request, 'userPanelApp/editProfile.html', {})


class changePasswordView(View):
    def get(self, request: HttpRequest):
        context = {
            'form': changePasswordForm()
        }
        return render(request, 'userPanelApp/changePassword.html', context)

    def post(self, request: HttpRequest):
        form = changePasswordForm(request.POST)
        if form.is_valid():
            currentUser: User = User.objects.filter(id=request.user.id).first()
            if currentUser.check_password(form.cleaned_data.get('current_password')):
                currentUser.set_password(form.cleaned_data.get('password'))
                currentUser.save()
                logout(request)
                return redirect(reverse('login-page'))
            else:
                form.add_error('password', 'کلمه عبور فعلی نادرست است')

        context = {
            'form': form
        }
        return render(request, 'userPanelApp/changePassword.html', context)


def panelPartial(request: HttpRequest):
    return render(request, 'userPanelApp/includes/panelPartial.html')
