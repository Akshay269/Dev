from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
        exclude=['password1','password2']


class UpdateProfileForm(forms.ModelForm):

    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:

        model = Profile
        fields = ['profile_pic']