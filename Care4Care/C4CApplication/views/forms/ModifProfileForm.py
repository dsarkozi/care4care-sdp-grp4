from django import forms

from C4CApplication.models.member import Member


class ModifProfileForm(forms.Form):

    #adresse
    number  = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'number', 'size' : 10}))
    street  = forms.CharField(max_length=100, widget=forms.TextInput(  attrs={'placeholder': 'street', 'size' : 32}))
    zip     = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'zip',    'size' : 10}))
    town    = forms.CharField(max_length=100, widget=forms.TextInput(  attrs={'placeholder': 'town',   'size' : 32}))
    picture = forms.ImageField()
    
    #infos facultatives
    fixed_phone  = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(attrs={'placeholder': 'fixed phone',' size' : 88  }))
    mobile_phone = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(attrs={'placeholder': 'mobile phone',' size' : 10}))

    #renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    