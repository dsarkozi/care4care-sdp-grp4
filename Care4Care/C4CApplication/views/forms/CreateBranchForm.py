from django import forms
from django.forms.widgets import TextInput, EmailInput


class CreateBranchForm(forms.Form):
    name = forms.CharField(
        widget=TextInput(
            attrs={'autofocus':'true', 'placeholder':'branch name'}
        ), label="Name of the branch "
    )
    
    town = forms.CharField(
        widget=TextInput(
            attrs={'placeholder':'town'}
        ), label="Name of the town "
    )
    
    branch_off = forms.EmailField(
        widget=EmailInput(
            attrs={'placeholder':'branch_officer@mail.com'}
        ), label="Branch officer mail"
    )
    
    address = forms.CharField(
        widget=TextInput(
            attrs={'placeholder':'number, street, postal code'}
        ), label="Name of the branch "
    )
    