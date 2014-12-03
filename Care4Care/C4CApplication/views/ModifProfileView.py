from django.views.generic.edit import FormView
from django.core.exceptions import PermissionDenied

from C4CApplication.models.member import Member
from C4CApplication.views.forms.ModifProfileForm import ModifProfileForm
from django.core.urlresolvers import reverse_lazy
from C4CApplication.views.utils import create_user


class ModifProfileView(FormView):
    model = Member
    template_name = 'C4CApplication/ModifProfile.html'
    form_class = ModifProfileForm
    user = None
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.user.db_member.mail})

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])

        return super(ModifProfileView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ModifProfileView, self).get_context_data(**kwargs)
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session
        return context
    
    def form_valid(self, form):
        #adresse
        number = form.cleaned_data['number']
        street = form.cleaned_data['street']
        zip_num = form.cleaned_data['zip']
        town = form.cleaned_data['town']
        #infos faculatives
        fixed_phone = form.cleaned_data['fixed_phone']
        mobile_phone = form.cleaned_data['mobile_phone']
        picture = form.cleaned_data['picture']
        if picture is not None:
            image_name = "%s" % self.user.db_member.mail
            image_name = image_name.replace('@', '.').replace('.', '')+".jpg"
            picture.name = image_name
            self.user.db_member.picture = picture
        
        self.user.db_member.mobile = mobile_phone
        self.user.db_member.telephone = fixed_phone
        
        self.user.db_member.address = street+ ", " + number + ", " + zip_num +", " +town

        self.user.db_member.save()
                  
        return super(ModifProfileView, self).form_valid(form)

    def get_initial(self):
        address = self.user.db_member.address
        table = address.split(',')
        #street+ ", " + number + ", " + zip +", " +town
        street = table[0]
        number = table[1][1:]
        zip = table[2][1:]
        town = table[3][1:]
        self.initial = {'number':number, 'street':street, 'zip':zip , 'town':town,'fixed_phone':self.user.db_member.telephone,  'mobile_phone':self.user.db_member.mobile}
        return self.initial.copy()
