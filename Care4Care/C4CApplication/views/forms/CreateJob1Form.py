from django import forms
from django.forms.widgets import TextInput

from C4CApplication.models.job import Job


class CreateJob1Form(forms.Form):
    title = forms.CharField(
        widget=TextInput(
            attrs={'autofocus':'true'}
        )
    )
    categories = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Job.CAT,
    )
    other = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={'placeholder':'Other'}
        )
    )
    categories.choices.extend([('other','other')])