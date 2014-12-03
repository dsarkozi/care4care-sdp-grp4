from django import forms

from C4CApplication.models.member import Member


class ModifProfileForm(forms.Form):

    new_password   = forms.CharField( max_length=100 , required=False , widget=forms.PasswordInput(attrs={'placeholder': 'new_password', 'size' : 44}))
    password   = forms.CharField( max_length=100  , widget=forms.PasswordInput(attrs={'placeholder': 'password', 'size' : 44}))

    #adresse
    number  = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'number', 'size' : 10}))
    street  = forms.CharField(max_length=100, widget=forms.TextInput(  attrs={'placeholder': 'street', 'size' : 32}))
    zip     = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'zip',    'size' : 10}))
    town    = forms.CharField(max_length=100, widget=forms.TextInput(  attrs={'placeholder': 'town',   'size' : 32}))
    picture = forms.ImageField()
    
    #infos facultatives
    fixed_phone  = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(attrs={'placeholder': 'fixed phone',' size' : 88  }))
    mobile_phone = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(attrs={'placeholder': 'mobile phone',' size' : 10}))

    #renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoy��.", required=False)
    
    def clean(self):
        cleaned_data = super(ModifProfileForm, self).clean()
        new_password = ''  
        new_password = cleaned_data.get('new_password')
        password = ''
        password = cleaned_data.get('new_password')
        
        #mot de passe
        if new_password:
            if len(new_password) <8 and len(new_password) !=0:
                msg = "Your password is too short, it should be at least 8 characters long."
                self.add_error("new_password",msg)
                
        

        #address: vérifier qu'il n'y a pas de , dans les champs de l'address
        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    