from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView
from django.http import HttpResponse
from . import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
class RegisterView(CreateView):
    template_name = "accounts/register.html"

    def get(self, request):
        form = forms.RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('Please meet the password criteria!')


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

    def get(self, request):
        user = request.user

        args = {'user': user}
        return render(request, self.template_name, args)

class ProfileEdit(UpdateView):
    template_name = "accounts/profile_edit.html"

    def get(self, request):
        form = forms.ProfileEditForm(instance=request.user)
        print(request.user)
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = forms.ProfileEditForm(request.POST, instance=request.user)
        args = {'form': form}

        if form.is_valid():
            form.save()
        return redirect('/accounts/profile')


class PasswordChange(UpdateView):
    template_name = "accounts/password_change.html"

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('password_change')