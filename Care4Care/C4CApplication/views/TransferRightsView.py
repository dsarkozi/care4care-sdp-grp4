from django.views.generic import FormView
from C4CApplication import models
from C4CApplication.meta import Member, User
from C4CApplication.views.forms.TransferRightsForm import TransferRightsForm
from C4CApplication.views.utils import create_user

from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


class TransferRightsView(FormView):
    template_name = "C4CApplication/TransferRights.html"
    form_class = TransferRightsForm
    success_url = reverse_lazy("myc4c")
    user = None
    
    """def get_object(self):
        job = super(ConfirmJobDoneView, self).get_object()
        return job"""
    
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

        context['transfer_rights_form'] = transfer_rights_form
        return context

    
    def form_valid(self, form):
        # TODO test if the member has session variables !! -> redirection
        if TransferRightsView.user is None:
            TransferRightsView.user = models.Member.objects.get(mail=self.request.session['email'])

        # value entered in the input field
        email_new_BPAdmin = form.cleaned_data['email_new_BPAdmin']
        member = models.Member.objects.filter(mail=email_new_BPAdmin)
        if len(member) == 0 : print("No such a member !") # pop up ?
        else : 
            member = member[0]
            # TODO do the transfer of right : set email_new_BPAdmin as BP Admin
            member.tag = Member.TAG['bp_admin']
            member.save()
            
            # remove rights of the current user ??
        
        return super(TransferRightsView, self).form_valid(form)