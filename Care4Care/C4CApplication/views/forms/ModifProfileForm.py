from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy
from C4CApplication.models.member import Member
from django.utils.translation import string_concat
from django.utils.translation import ugettext_lazy


class ModifProfileForm(forms.Form):

    new_password   = forms.CharField( min_length=8, max_length=100 , required=False , widget=forms.PasswordInput(attrs={'placeholder': _('new password'), 'size' : 44}))
    password   = forms.CharField( min_length=8, max_length=100 , required=False  , widget=forms.PasswordInput(attrs={'placeholder': _('password verification'), 'size' : 44}))
    affiche = _('street, number, more informations')#_('street, number, more informations')
    #affiche = _('lol, vieux, con')
    #adresse
    street  = forms.CharField(max_length=100, widget=forms.TextInput(  attrs={'placeholder': affiche, 'size' : 32}))
    zip     = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'placeholder': _('zip'),    'size' : 10}))
    town    = forms.CharField(max_length=100, widget=forms.TextInput(  attrs={'placeholder': _('town'),   'size' : 32}))
    
    #infos facultatives
    picture = forms.ImageField(required=False)
    fixed_phone  = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(attrs={'placeholder': _('fixed phone'),' size' : 88  }))
    mobile_phone = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(attrs={'placeholder': _('mobile phone'),' size' : 10}))
    
    def clean(self):
        cleaned_data = super(ModifProfileForm, self).clean()
        new_password = ''  
        new_password = cleaned_data.get('new_password')
        password = ''
        password = cleaned_data.get('password')
        
        #mot de passe
        if new_password:
            if len(new_password) <8 and len(new_password) !=0:
                msg = _("Your password is too short, it should be at least 8 characters long.")
                self.add_error("new_password",msg)
            if new_password!=password:
                msg = _("You entered different passwords")
                self.add_error("new_password",msg)
        

        #address: verifier qu'il n'y a pas de , dans les champs de l'address
        return cleaned_data  # N'oublions pas de renvoyer les donnees si tout est OK
    
    
    
    
    
    
    
    
    
