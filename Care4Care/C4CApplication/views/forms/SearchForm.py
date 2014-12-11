from django import forms
from django.forms.widgets import EmailInput
from django.utils.translation import ugettext_lazy as _


class SearchForm(forms.Form):

    email_member = forms.EmailField(
        widget=EmailInput(
            attrs={'autofocus':'true', 'placeholder':'member@mail.com'}
        ), label=_("Filter the jobs created by the member"), required=False
    )

    type_of_job = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(('offer', _('See help offers')), ('demand', _('See help demands')))
    )