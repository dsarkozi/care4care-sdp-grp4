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

    def clean(self):
        """
        Overrides clean from super to add an error if 'other' has been checked,
        but nothing was provided in the text field.
        """
        cleaned_data = super(CreateJob1Form, self).clean()
        category = cleaned_data.get("categories")
        other = cleaned_data.get("other")
        if category == 'other' and other == '':
            self.add_error("other", forms.ValidationError("If other is checked, fill the text input in.", code='missing'))
        return cleaned_data