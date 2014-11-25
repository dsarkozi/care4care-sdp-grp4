from django import forms
from C4CApplication.models.member import Member


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
        widget=forms.RadioSelect,
        choices=(('c4c', 'Send to the Care4Care company'), ('user', 'Send to user'))
    )
    userDropdown = forms.ChoiceField(
        widget=forms.Select,
        choices=Member.objects.values_list('mail','first_name')
    )