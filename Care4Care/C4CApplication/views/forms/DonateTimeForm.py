from django import forms


class DonateTimeForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':'5'}
        )
    )
    donation = forms.MultiValueField(
        fields=(
            forms.CharField(error_messages={'incomplete':'Enter a donation amount.'}),
            forms.CharField(error_messages={'incomplete':'Enter a donation amount.'}),
            forms.CharField(error_messages={'incomplete':'Enter a donation amount.'})
        ),
        error_messages={'incomplete':'Enter a donation amount.'}
    )
    receiver = forms.ChoiceField(
        widget=forms.RadioSelect
    )