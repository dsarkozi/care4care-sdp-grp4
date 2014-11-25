from django import forms
from django.forms.widgets import NumberInput  

class ConfirmJobDoneForm(forms.Form): 
    time_to_pay = forms.IntegerField(
        widget=NumberInput(
            attrs={'placeholder': 'Time allowance', 'autofocus': 'true'}
        )
    )
    # Note : django avoid using NumberInput for field having localize property to True
    
    def post(self, request, *args, **kwargs): 
        member = None # TODO variable de session
        
        # recupere la valeur d'input
        # verifier que cette valeur est ok
        
        member.register_job_done(job_id, helped_one_email) # comment je connais le job ?
        
        super(ConfirmJobDoneForm, self).post(request, *args, **kwargs)