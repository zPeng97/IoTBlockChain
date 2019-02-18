from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


#Create forms here
class RegistrationForm(UserCreationForm):
    #image = forms.ImageField(upload_to='profile_image', blank=True)
    email = forms.EmailField(required=True)
    company = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=12)


    class Meta:
        model = User
        fields = (
            'username',
            #'image',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'company',
            'contact'
        )

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #
    #     return user

class ProfileEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
        }

