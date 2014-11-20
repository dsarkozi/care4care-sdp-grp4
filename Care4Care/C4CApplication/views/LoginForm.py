from django import forms
from django.forms.widgets import EmailInput, PasswordInput


class LoginForm(forms.Form):
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'login-input', 'placeholder': 'Email Address', 'autofocus': 'true'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'login-input', 'placeholder': 'Password'}))

