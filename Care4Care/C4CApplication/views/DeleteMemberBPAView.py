from django.views.generic import FormView
from C4CApplication import models
from C4CApplication.meta import Member, User
#from C4CApplication.views.TransferRightsView import TransferRightsView
from C4CApplication.views.forms.DeleteMemberBPAForm import DeleteMemberBPAForm
from C4CApplication.views.utils import create_user

from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


class DeleteMemberBPAView(FormView):
    template_name = "C4CApplication/DeleteMemberBPA.html"
    form_class = DeleteMemberBPAForm
    success_url = reverse_lazy("myc4c")
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])
        
        return super(DeleteMemberBPAView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(DeleteMemberBPAView, self).get_context_data(**kwargs)
        
        # Creates the form and change the context
        delete_member_bpa_form = DeleteMemberBPAForm(auto_id=False)

        context['delete_member_bpa_form'] = delete_member_bpa_form
        return context

    
    def form_valid(self, form):
        # TODO test if the member has session variables !! -> redirection
        if DeleteMemberBPAView.user is None:
            DeleteMemberBPAView.user = models.Member.objects.get(mail=self.request.session['email'])

        # value entered in the input field
        email_deleted_one = form.cleaned_data['email_deleted_one']
        
        user = create_user(email_deleted_one)
        if user is not None : user.delete()
        else : print("No such a member !") # pop up ?
        
        return super(DeleteMemberBPAView, self).form_valid(form)