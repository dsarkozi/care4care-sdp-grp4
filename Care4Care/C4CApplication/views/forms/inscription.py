#-*- coding: utf-8 -*-
from C4CApplication.models import *
from django import forms

class InscriptionForm(forms.Form):
#infos perso
    #widget=forms.TextInput(attrs={'placeholder': 'Email' , 'size' : 44})
    prenom = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': 'prénom' , 'size' : 21}))
    nom = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': 'nom' , 'size' : 21}))
    email = forms.EmailField( max_length=100  , widget=forms.TextInput(attrs={'placeholder': 'Email' , 'size' : 44}))
    mot_de_passe = forms.CharField( max_length=100  , widget=forms.PasswordInput(attrs={'placeholder': 'mot de passe' , 'size' : 44}))
    date_de_naissance = forms.CharField( max_length=100  , widget=forms.TextInput(attrs={'placeholder': 'jj/mm/aaaa' , 'size' : 44}))
    #adresse
    numero =            forms.CharField( max_length=100  , widget=forms.NumberInput(attrs={'placeholder': 'numero' , 'size' : 10}))
    rue =    forms.CharField( max_length=100,   widget=forms.TextInput(attrs={'placeholder': 'rue' , 'size' : 32}))
    code_postal = forms.CharField( max_length=100  , widget=forms.NumberInput(attrs={'placeholder': 'code_postal' , 'size' : 10}))
    ville = forms.CharField( max_length=100  , widget=forms.TextInput(attrs={'placeholder': 'ville',' size' : 32}))
#type de membre
    CHOICES = (('1', 'non membre (valeur par defaut)'), ('2', 'membre'),('4','verified'),('8','volunteer'),('16','branch officer'),('32','bp administrator'))
    
        
    
    BRANCH_CHOICES = ()
    branch = Branch.objects.all()
    for b in branch:
        BRANCH_CHOICES = BRANCH_CHOICES +((b.name,b.name),)
    
    #(('aucune', 'aucune'), ('bruxelles', 'bruxelles'))
    
    type_membre = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    branch = forms.CharField(max_length=3,
                widget=forms.Select(choices=BRANCH_CHOICES))
    naissance = birth_date = forms.DateField(required=False)

    
#infos facultatives
    telephone_fixe = forms.CharField( max_length=100 , required=False , widget=forms.NumberInput(attrs={'placeholder': 'telephone fixe',' size' : 88  }))
    telephone_mobile = forms.CharField( max_length=100 , required=False , widget=forms.NumberInput(attrs={'placeholder': 'telephone mobile',' size' : 10}))



    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
    def clean(self):              
                isin = False
                members = Member.objects.all()

                cleaned_data = super(InscriptionForm, self).clean()
                email = cleaned_data.get('email')        
                
                if email:
                    for mem in members:
                        if mem.mail in email:
                            isin = True
                            break
                            #if  "olivier.bonaventure@gmail.com" in receveur:  # Est-ce que sujet et message sont valides ?
                        
                if  isin:                #raise forms.ValidationError("Vous parlez de pizzas dans le sujet ET le message ? Non mais ho !")
                    msg = "a count with these email address already exist."
                    self.add_error("email", msg)
                return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK
    

