from django import forms
from django.forms.widgets import EmailInput, PasswordInput


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=EmailInput(attrs={'class': 'login-input', 'placeholder': 'Email Address', 'autofocus': 'true'}))
    password = forms.CharField(required=True, widget=PasswordInput(attrs={'class': 'login-input', 'placeholder': 'Password'}))