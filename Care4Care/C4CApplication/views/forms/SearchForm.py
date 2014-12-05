from django import forms
from django.forms.widgets import TextInput, EmailInput

from C4CApplication.models.job import Job


class SearchForm(forms.Form):

    email_member = forms.EmailField(
        widget=EmailInput(
            attrs={'autofocus':'true', 'placeholder':'member@mail.com'}
        ), label="Filter the jobs created by the member", required=False
    )

    type_of_job = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(('offer', 'See help offers'), ('demand', 'Send help demands'))
    )