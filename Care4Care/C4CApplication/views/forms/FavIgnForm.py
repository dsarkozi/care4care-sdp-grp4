from django import forms
from django.forms.widgets import EmailInput


class FavIgnForm(forms.Form):
     email = forms.EmailField(
        widget=EmailInput(
            attrs={'class': 'favorite-input', 'placeholder': 'Email Address', 'autofocus': 'true', 'font-size': '16px',
                   'style':'width:100%'}
        )
    )