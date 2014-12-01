#-*- coding: utf-8 -*-
from C4CApplication.models import *
from django import forms

class InscriptionForm(forms.Form):
#infos perso
    #widget=forms.TextInput(attrs={'placeholder': 'Email' , 'size' : 44})
    first_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': 'first name' , 'size' : 21}))
    last_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': 'last name' , 'size' : 21}))
    email = forms.EmailField( max_length=100  , widget=forms.TextInput(attrs={'placeholder': 'email' , 'size' : 44}))
    password = forms.CharField( max_length=100  , widget=forms.PasswordInput(attrs={'placeholder': 'password' , 'size' : 44}))
    birthdate = forms.CharField( max_length=100  , widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd' , 'size' : 44}))
    #adresse
    number = forms.CharField( max_length=100  , widget=forms.NumberInput(attrs={'placeholder': 'number' , 'size' : 10}))
    street = forms.CharField( max_length=100,   widget=forms.TextInput(attrs={'placeholder': 'street' , 'size' : 32}))
    zip = forms.CharField( max_length=100  , widget=forms.NumberInput(attrs={'placeholder': 'zip' , 'size' : 10}))
    town = forms.CharField( max_length=100  , widget=forms.TextInput(attrs={'placeholder': 'town',' size' : 32}))
#type de membre
    CHOICES = (('1', 'non membre (valeur par defaut)'), ('2', 'membre'),('4','verified'),('8','volunteer'),('16','branch officer'),('32','bp administrator'))
    
        
    
    BRANCH_CHOICES = ()
    branch = Branch.objects.all()
    for b in branch:
        BRANCH_CHOICES = BRANCH_CHOICES +((b.name,b.name),)
    
    #(('aucune', 'aucune'), ('bruxelles', 'bruxelles'))
    
    #member_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    member_type = forms.MultipleChoiceField(widget=forms.RadioSelect(), choices=CHOICES)
    branch = forms.CharField(widget=forms.Select(choices=BRANCH_CHOICES))
    #birth_date = forms.DateField(required=False)

    
#infos facultatives
    fixe_phone = forms.CharField( max_length=100 , required=False , widget=forms.NumberInput(attrs={'placeholder': 'fixe phone',' size' : 10  }))
    mobile_phone = forms.CharField( max_length=100 , required=False , widget=forms.NumberInput(attrs={'placeholder': 'mobile phone',' size' : 10}))



    #renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
    def clean(self):
        isin = False
        members = Member.objects.all()
        birthdate = ''
        cleaned_data = super(InscriptionForm, self).clean()
        email = cleaned_data.get('email')
        password = ''  
        birthdate = cleaned_data.get('birthdate')
        password = cleaned_data.get('password')
        #email
        if email:
            for mem in members:
                if mem.mail in email:
                    isin = True
                    break
                    #if  "olivier.bonaventure@gmail.com" in receveur:  # Est-ce que sujet et message sont valides ?
                
        if  isin:                #raise forms.ValidationError("Vous parlez de pizzas dans le sujet ET le message ? Non mais ho !")
            msg = "An account with these email address already exist."
            self.add_error("email", msg)
            
        #date
        if birthdate:
            if not len(birthdate) is 10:
                msg = "Date has an invalid format."
                self.add_error("birthdate",msg)
            elif ( not birthdate[0].isdigit()) or (not birthdate[1].isdigit())or (not birthdate[2].isdigit())or (not birthdate[3].isdigit()) or (not birthdate[4] is '-') or (not birthdate[5].isdigit()) or (not birthdate[6].isdigit()) or (not birthdate[7] is '-') or (not birthdate[8].isdigit()) or (not birthdate[9].isdigit()):                       
                msg = "Date has an invalid format."
                self.add_error("birthdate",msg)
            elif not(birthdate[5] is '0' or birthdate[5] is '1'):
                msg = "Date has an invalid format."
                self.add_error("birthdate",msg)
            elif not ((birthdate[8] is '0' )or (birthdate[8] is '1') or(birthdate[8] is '2') or (birthdate[8] is '3')):
                msg = "Date has an invalid format."
                self.add_error("birthdate",msg)
            #février et date bisextile
            #année de naissance plosible
        
        #mot de passe
        if password:
            if len(password) <8:
                msg = "Your password is too short, it should be at least 8 characters long."
                self.add_error("password",msg)
                
        #address: vérifier qu'il n'y a pas de , dans les champs de l'address
        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK