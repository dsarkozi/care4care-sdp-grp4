from django.views.generic import FormView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy

from C4CApplication import models
from C4CApplication.views.forms.TransferRightsForm import TransferRightsForm
from C4CApplication.views.utils import create_user


class TransferRightsView(FormView):
    template_name = "C4CApplication/TransferRights.html"
    form_class = TransferRightsForm
    success_url = reverse_lazy("profile")
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])
        
        return super(TransferRightsView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(TransferRightsView, self).get_context_data(**kwargs)
        
        # Creates the form and change the context
        transfer_rights_form = TransferRightsForm(auto_id=False)
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session
        context['transfer_rights_form'] = transfer_rights_form
        return context
    
    def form_valid(self, form):
        if TransferRightsView.user is None:
            TransferRightsView.user = models.Member.objects.get(mail=self.request.session['email'])

        # value entered in the input field
        email_new_BPAdmin = form.cleaned_data['email_new_BPAdmin']
        
        res = self.user.transfer_bp_admin_rights(email_new_BPAdmin)
        if not res:
            return super(TransferRightsView, self).form_invalid(form)
        
        return super(TransferRightsView, self).form_valid(form)