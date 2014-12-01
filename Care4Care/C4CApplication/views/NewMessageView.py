from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from C4CApplication.views.forms.nouveauMessageForm import Nouveau_messageForm
from C4CApplication.models import *
from C4CApplication.views.utils import create_user

from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

class NewMessageView(FormView):
    model = Message
    template_name = 'C4CApplication/nouveau_message.html'
    form_class = Nouveau_messageForm
    success_url = reverse_lazy('newmessage')

    def form_valid(self, form):
            email_envoyeur = "kim.mens@gmail.com"
            member = create_user(email_envoyeur)
            
            sujet = form.cleaned_data['sujet']
            receveur = form.cleaned_data['receveur']
            message = form.cleaned_data['message']
            renvoi = form.cleaned_data['renvoi']
            #sender_mail, receiver_mail, subject, content, type): #TODO type

            member.send_mail(email_envoyeur,receveur,sujet,message,2)
        
            return super(NewMessageView, self).form_valid(form)
   
"""
def nouveau_message(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = Nouveau_messageForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            #member = Member.objects.filter(mail=request.session['email'])
            email_envoyeur = "kim.mens@gmail.com"
            member = Member(email_envoyeur)
            
            sujet = form.cleaned_data['sujet']
            receveur = form.cleaned_data['receveur']
            message = form.cleaned_data['message']
            renvoi = form.cleaned_data['renvoi']
            #sender_mail, receiver_mail, subject, content, type): #TODO type

            member.send_mail(email_envoyeur,receveur,sujet,message,2)
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = Nouveau_messageForm()  # Nous créons un formulaire vide

    return render(request, 'C4CApplication/nouveau_message.html', locals())

"""