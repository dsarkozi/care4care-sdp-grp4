from django.views.generic.edit import FormView
from django.core.exceptions import PermissionDenied

from C4CApplication.models.member import Member
from C4CApplication.views.forms.modifProfileForm import ModifProfileForm
from django.core.urlresolvers import reverse_lazy


class ModifProfile(FormView):
    model = Member
    template_name = 'C4CApplication/modif_profile.html'
    form_class = ModifProfileForm
    success_url = reverse_lazy('modifprofile')

    def form_valid(self, form):
        
        #adresse
        numero = form.cleaned_data['numero']
        rue = form.cleaned_data['rue']
        code_postal = form.cleaned_data['code_postal']
        ville = form.cleaned_data['ville']
        #infos faculatives
        telephone_fixe = form.cleaned_data['telephone_fixe']
        telephone_mobile = form.cleaned_data['telephone_mobile']
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
        member.save()"""
        
        
        return super(Inscription, self).form_valid(form)


    def get_initial(self):
        return self.initial.copy()
