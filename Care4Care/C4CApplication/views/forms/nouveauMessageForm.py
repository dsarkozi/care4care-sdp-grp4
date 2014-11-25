#-*- coding: utf-8 -*-

from django import forms

class Nouveau_messageForm(forms.Form):

    receveur = forms.EmailField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': 'a:'}))
    sujet = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'placeholder': 'sujet:'}) , required=False  )
    message = forms.CharField(widget=forms.Textarea(attrs = {'placeholder': 'votre message'})  )
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoye.", required=False)
