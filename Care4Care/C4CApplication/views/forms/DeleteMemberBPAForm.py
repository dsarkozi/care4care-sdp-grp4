from django import forms
from django.forms.widgets import EmailInput
from django.utils.translation import ugettext_lazy as _


class DeleteMemberBPAForm(forms.Form):
    # text input for mail of new BP Admin
    email_deleted_one = forms.EmailField(
        widget=EmailInput(
            attrs={'autofocus':'true', 'placeholder':'member_to_delete@mail.com'}
        ), label=""
    )