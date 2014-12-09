from django.views.generic import FormView
from C4CApplication import models
from C4CApplication.meta import Member, User
from C4CApplication.views.forms.DeleteMemberBPAForm import DeleteMemberBPAForm
from C4CApplication.views.utils import create_user

from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


class DeleteMemberBPAView(FormView):
    template_name = "C4CApplication/DeleteMemberBPA.html"
    form_class = DeleteMemberBPAForm
    success_url = reverse_lazy("profile")
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
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session

        context['delete_member_bpa_form'] = delete_member_bpa_form
        return context

    def form_valid(self, form):
        if DeleteMemberBPAView.user is None:
            DeleteMemberBPAView.user = models.Member.objects.get(mail=self.request.session['email'])

        # value entered in the input field
        email_deleted_one = form.cleaned_data['email_deleted_one']

        self.user.delete_member_from_site(email_deleted_one)
        
        return super(DeleteMemberBPAView, self).form_valid(form)