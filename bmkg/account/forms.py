from django import forms
from .models import Akun
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class AkunForm(forms.ModelForm):

     class Meta():
         model = Akun
         fields = ('portfolio_site',)#'profile_pic')

