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
    
    street = forms.CharField(
        widget=TextInput(
            attrs={'placeholder':'street, number, more details'}
        ), label="Street of the branch "
    )
    
    zip = forms.CharField(
        widget=TextInput(
            attrs={'placeholder':'postal code'}
        ), label="Zip of the branch "
    )
    
    town = forms.CharField(
        widget=TextInput(
            attrs={'placeholder':'town'}
        ), label="Town of the branch "
    )
    