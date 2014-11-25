#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect

from C4CApplication.views.forms.inscription import InscriptionForm

def inscription(request):
 # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InscriptionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():


            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #infos perso
            prenom = form.cleaned_data['prenom']
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            date_de_naissance = form.cleaned_data['date_de_naissance']
            #adresse
            numero = form.cleaned_data['numero']
            rue = form.cleaned_data['rue']
            code_postal = form.cleaned_data['code_postal']
            ville = form.cleaned_data['ville']
            #type de membre
            type_membre = form.cleaned_data['type_membre']
            branch = form.cleaned_data['branch']

            #infos faculatives
            telephone_fixe = form.cleaned_data['telephone_fixe']
            telephone_mobile = form.cleaned_data['telephone_mobile']
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InscriptionForm()

    return render(request, 'C4CApplication/inscription.html', locals())

