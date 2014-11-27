#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from C4CApplication.models import * 

from C4CApplication.views.forms.inscription import InscriptionForm

from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

class Inscription(FormView):
    model = Member
    template_name = 'C4CApplication/inscription.html'
    form_class = InscriptionForm
    success_url = reverse_lazy('inscription')

    def form_valid(self, form):
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
         
        member = model.Member(mail = email )
        member.password = mot_de_passe
        member.first_name = prenom
        member.last_name = nom
        member.birthday = date_de_naissance
        member.tag = Member.TAG_REVERSE[type_membre]
        
        #adresse
        member.address = rue+ ", " + numero + ", " + code_postal +", " +ville
        
        member.telephone = telephone_fixe
        member.mobile = telephonde_mobile
        member.save()
        member.branch.add(Branch.objects.get(name = branch))
        
        
        return super(Inscription, self).form_valid(form)

"""
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
"""
"""  
            member = models.Member(mail = email )
            member.password = mot_de_passe
            member.first_name = prenom
            member.last_name = nom
            member.birthday = date_de_naissance
            member.tag = Member.TAG_REVERSE[type_membre]
            #adresse
            member.address = numero+ " " + rue + " "+ " " + code_postal +" " +ville
            
            member.mobile = telephonde_mobile
            member.address = "Rue de l'Eglise, 40, Rixensart, 1330"
            member.time_credit = 9999
            member.save()
"""
"""
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InscriptionForm()

    return render(request, 'C4CApplication/inscription.html', locals())
"""
