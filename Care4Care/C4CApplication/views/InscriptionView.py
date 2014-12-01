#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from C4CApplication.models import * 

from C4CApplication.views.forms.InscriptionForm import InscriptionForm

from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

class InscriptionView(FormView):
    model = Member
    template_name = 'C4CApplication/inscription.html'
    form_class = InscriptionForm
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        birthdate = form.cleaned_data['birthdate']
        #adresse
        number = form.cleaned_data['number']
        street = form.cleaned_data['street']
        zip = form.cleaned_data['zip']
        town = form.cleaned_data['town']
        #type de membre
        member_type = form.cleaned_data['member_type']
        branch = form.cleaned_data['branch']
            #infos faculatives
        telephone_fixe = form.cleaned_data['fixe_phone']
        telephone_mobile = form.cleaned_data['mobile_phone']
         
        member = Member(mail = email )
        member.password = password
        member.first_name = first_name
        member.last_name = last_name
        member.birthday = birthdate
        member.tag = int(member_type)
        
        #adresse
        member.address = street+ ", " + number + ", " + zip +", " +town
        
        member.telephone = telephone_fixe
        member.mobile = telephone_mobile
        member.save()
        member.branch.add(Branch.objects.get(name = branch))
        
        
        return super(InscriptionView, self).form_valid(form)

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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            birthdate = form.cleaned_data['birthdate']
            #adresse
            number = form.cleaned_data['number']
            street = form.cleaned_data['street']
            zip = form.cleaned_data['zip']
            town = form.cleaned_data['town']
            #type de membre
            member_type = form.cleaned_data['member_type']
            branch = form.cleaned_data['branch']

            #infos faculatives
            telephone_fixe = form.cleaned_data['telephone_fixe']
            telephone_mobile = form.cleaned_data['telephone_mobile']
"""
"""  
            member = models.Member(mail = email )
            member.password = password
            member.first_name = first_name
            member.last_name = last_name
            member.birthday = birthdate
            member.tag = Member.TAG_REVERSE[member_type]
            #adresse
            member.address = number+ " " + street + " "+ " " + zip +" " +town
            
            member.mobile = telephonde_mobile
            member.address = "street de l'Eglise, 40, Rixensart, 1330"
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
