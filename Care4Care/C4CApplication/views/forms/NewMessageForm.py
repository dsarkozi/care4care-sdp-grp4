
from django import forms
from C4CApplication.models import * 


class NewMessageForm(forms.Form):

    receveur = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'to:'}))
    sujet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'subject:'}), required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'your message'}))
    
    def clean(self):              
                isin = False
                members = Member.objects.all()

                cleaned_data = super(NewMessageForm, self).clean()
                receveur = cleaned_data.get('receveur')        
                
                if receveur:
                    for mem in members:
                        if mem.mail in receveur:
                            isin = True
                            break
                            #if  "olivier.bonaventure@gmail.com" in receveur:  # Est-ce que sujet et message sont valides ?
                        
                if  not isin:                #raise forms.ValidationError("Vous parlez de pizzas dans le sujet ET le message ? Non mais ho !")
                    msg = "these Email addresse doesn't exist"
                    self.add_error("receveur", msg)
                return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK
    
#class CronForm(forms.Form):
#   days = forms.ModelChoiceField(queryset=Message.objects.all().order_by('date'))