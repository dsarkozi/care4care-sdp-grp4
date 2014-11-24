from django import forms
from django.forms.widgets import NumberInput # EmailInput, PasswordInput # 

class ConfirmJobDoneForm(forms.Form): 
    time_to_pay = forms.IntegerField(
        widget=NumberInput(
            attrs={'placeholder': 'Time allowance for the job', 'autofocus': 'true'}
        )
    )
    # Note : django avoid using NumberInput for field having localize property to True
    