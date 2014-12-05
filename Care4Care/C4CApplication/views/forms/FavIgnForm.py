from django import forms
from django.forms.widgets import EmailInput
from django.utils.translation import ugettext_lazy as _


class FavIgnForm(forms.Form):
     email = forms.EmailField(
        widget=EmailInput(
            attrs={'class': 'favorite-input', 'placeholder': _('Email Address'), 'autofocus': 'true', 'font-size': '16px',
                   'style':'width:100%'}
        )
    )