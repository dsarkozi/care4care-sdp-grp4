#-*- coding: utf-8 -*-

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
    CHOICES = (('1', 'non membre (valeur par defaut)'), ('2', 'membre'))
    BRANCH_CHOICES = (('aucune', 'aucune'), ('bruxelles', 'bruxelles'))

    type_membre = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    branch = forms.CharField(max_length=3,
                widget=forms.Select(choices=BRANCH_CHOICES))
    naissance = birth_date = forms.DateField(required=False)

    
#infos facultatives
    telephone_fixe = forms.CharField( max_length=100 , required=False , widget=forms.NumberInput(attrs={'placeholder': 'telephone fixe',' size' : 88  }))
    telephone_mobile = forms.CharField( max_length=100 , required=False , widget=forms.NumberInput(attrs={'placeholder': 'telephone mobile',' size' : 10}))



    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    


class Nouveau_messageForm(forms.Form):

    receveur = forms.EmailField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': 'a:'}))
    sujet = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': 'sujet:'}) , required=False  )
    message = forms.CharField(widget=forms.Textarea(attrs = {'placeholder': 'votre message'})  )
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoye.", required=False)

