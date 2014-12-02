from django.views.generic.edit import FormView
from django.core.exceptions import PermissionDenied

from C4CApplication.models.member import Member
from C4CApplication.views.forms.ModifProfileForm import ModifProfileForm
from django.core.urlresolvers import reverse_lazy
from C4CApplication.views.utils import create_user


class ModifProfileView(FormView):
    model = Member
    template_name = 'C4CApplication/modif_profile.html'
    form_class = ModifProfileForm
    success_url = reverse_lazy('home')

    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])

        return super(ModifProfileView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ModifProfileView, self).get_context_data(**kwargs)
        context['member'] = self.user.db_member
        return context
    
    def form_valid(self, form):       
        #adresse
        numero = form.cleaned_data['numero']
        rue = form.cleaned_data['rue']
        code_postal = form.cleaned_data['code_postal']
        ville = form.cleaned_data['ville']
        #infos faculatives
        telephone_fixe = form.cleaned_data['telephone_fixe']
        telephone_mobile = form.cleaned_data['telephone_mobile']
        
        self.user.db_member.mobile = telephone_mobile
        self.user.db_member.telephone = telephone_fixe
        
        self.user.db_member.address = rue+ ", " + numero + ", " + code_postal +", " +ville
        self.user.db_member.save()
                  
        return super(ModifProfileView, self).form_valid(form)
        


    def get_initial(self):
        address = self.user.db_member.address
        table = address.split(',')
        #rue+ ", " + numero + ", " + code_postal +", " +ville
        rue = table[0]
        numero = table[1][1:]
        code_postal = table[2][1:]
        ville = table[3][1:]
        self.initial = {'numero':numero, 'rue':rue, 'code_postal':code_postal , 'ville':ville,'telephone_fixe':self.user.db_member.telephone,  'telephone_mobile':self.user.db_member.mobile}
        return self.initial.copy()

