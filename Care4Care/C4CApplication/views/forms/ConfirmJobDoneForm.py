from django import forms
from django.forms.widgets import NumberInput  
from django.utils.translation import ugettext_lazy as _


class ConfirmJobDoneForm(forms.Form): 
    time_to_pay = forms.IntegerField(
        widget=NumberInput(
            attrs={'placeholder': _('Time allowance'), 'autofocus': 'true'}
        ), min_value=0, label=""
    )
    # Note : django avoid using NumberInput for field having localize property to True
    