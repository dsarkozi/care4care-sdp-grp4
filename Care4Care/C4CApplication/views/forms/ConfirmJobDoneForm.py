from django import forms
from django.forms.widgets import NumberInput  

class ConfirmJobDoneForm(forms.Form): 
    time_to_pay = forms.IntegerField(
        widget=NumberInput(
            attrs={'placeholder': 'Time allowance', 'autofocus': 'true'}
        )
    )
    # Note : django avoid using NumberInput for field having localize property to True
    