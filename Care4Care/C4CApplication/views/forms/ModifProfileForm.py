from django import forms

from C4CApplication.models.member import Member


class ModifProfileForm(forms.Form):

    #adresse
    numero      = forms.CharField( max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'numero' , 'size' : 10}))
    rue         = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder': 'rue' , 'size' : 32}))
    code_postal = forms.CharField( max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'code_postal' , 'size' : 10}))
    ville       = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ville',' size' : 32}))
    
#infos facultatives
    telephone_fixe = forms.CharField( max_length=100 , required=False , widget=forms.NumberInput(attrs={'placeholder': 'telephone fixe',' size' : 88  }))
    telephone_mobile = forms.CharField( max_length=100 , required=False , widget=forms.NumberInput(attrs={'placeholder': 'telephone mobile',' size' : 10}))

    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    