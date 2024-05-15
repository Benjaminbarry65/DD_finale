from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login 
        fields = ['username', 'password']


class RegForm(UserCreationForm):
    class Meta:
        model = User   
        fields = ['username', 'password1', 'password2']     
