import decimal
from django import forms


class DonateTimeForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':'5'}
        )
    )
    days = forms.DecimalField(
        min_value=0
    )
    hours = forms.DecimalField(
        min_value=0
    )
    minutes = forms.DecimalField(
        min_value=0
    )
    receiver = forms.ChoiceField(
        widget=forms.RadioSelect
    )