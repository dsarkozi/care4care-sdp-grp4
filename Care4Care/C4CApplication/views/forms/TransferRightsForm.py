from django import forms
from django.forms.widgets import EmailInput
from django.utils.translation import ugettext_lazy as _


class TransferRightsForm(forms.Form):
    # text input for mail of new BP Admin
    email_new_BPAdmin = forms.EmailField(
        widget=EmailInput(
            attrs={'autofocus':'true', 'placeholder':_('new_BP_Admin@mail.com')}
        ), label=""
    )