from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUp(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name','last_name','username','email','password1','password2']
        

class Userdetails(forms.ModelForm):
    class Meta:
        model=UserDetails
        fields="__all__"
