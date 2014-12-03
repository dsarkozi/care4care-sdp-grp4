from django import forms

from C4CApplication.models.member import Member


class ModifProfileForm(forms.Form):

    #adresse
    number  = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'number', 'size' : 10}))
    street  = forms.CharField(max_length=100, widget=forms.TextInput(  attrs={'placeholder': 'street', 'size' : 32}))
    zip     = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'zip',    'size' : 10}))
    town    = forms.CharField(max_length=100, widget=forms.TextInput(  attrs={'placeholder': 'town',   'size' : 32}))
    
    #infos facultatives
    picture = forms.ImageField(required=False)
    fixed_phone  = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(attrs={'placeholder': 'fixed phone',' size' : 88  }))
    mobile_phone = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(attrs={'placeholder': 'mobile phone',' size' : 10}))
