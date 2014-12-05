from django.views.generic.edit import FormView
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from C4CApplication.views.forms.DonateTimeForm import DonateTimeForm
from django.core.urlresolvers import reverse_lazy
from C4CApplication.models.member import Member


class DonateTimeView(FormView):
    template_name = "C4CApplication/DonateTime.html"
    form_class = DonateTimeForm

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(DonateTimeView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        context = super(DonateTimeView, self).get_context_data(**kwargs)
        context['donateTime'] = DonateTimeForm(db_member=self.user.db_member, auto_id=False)
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session
        return context
    
    def form_valid(self, form):
        message = form.cleaned_data['message']

        days = form.cleaned_data['days']
        hours = form.cleaned_data['hours']
        minutes = form.cleaned_data['minutes']
        time = days*1440+hours*60+minutes
        
        receiver = form.cleaned_data['receiver']
        if receiver == 'c4c' :
            branchDropdown = form.cleaned_data['branchDropdown']
            self.user.make_donation(time, branchDropdown)
        else :
            userDropdown = form.cleaned_data['userDropdown']
            self.user.transfer_time(userDropdown, time)
        
        return super(DonateTimeView, self).form_valid(form)
            
            
            
            
            
            