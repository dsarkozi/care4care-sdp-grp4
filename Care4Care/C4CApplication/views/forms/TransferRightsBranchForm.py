from django import forms
from django.forms.widgets import EmailInput


class TransferRightsBranchForm(forms.Form):
    # text input for mail of new branch officer
    email_new_branch_officer = forms.EmailField(
        widget=EmailInput(
            attrs={'autofocus':'true', 'placeholder':'new_branch_officer@mail.com'}
        ), label=""
    )