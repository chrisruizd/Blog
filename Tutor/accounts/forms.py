from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #fname = forms.CharField(max_length=25)
    #lname = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']