from django.views.generic import FormView
from C4CApplication import models
from C4CApplication.meta import Member, User
from C4CApplication.views.TransferRightsView import TransferRightsView
from C4CApplication.views.forms.CreateBranchForm import CreateBranchForm
from C4CApplication.views.utils import create_user

from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


class CreateBranchView(FormView):
    template_name = "C4CApplication/CreateBranch.html"
    form_class = CreateBranchForm
    success_url = reverse_lazy("myc4c")
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])
        
        return super(CreateBranchView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(CreateBranchView, self).get_context_data(**kwargs)
        
        # Creates the form and change the context
        create_branch_form = CreateBranchForm(auto_id=False)

        context['create_branch_form'] = create_branch_form
        return context

    
    def form_valid(self, form):
        # TODO test if the member has session variables !! -> redirection
        if CreateBranchView.user is None:
            CreateBranchView.user = models.Member.objects.get(mail=self.request.session['email'])

        # value entered in the input field
        name = form.cleaned_data['name']
        print(name)
        
        # TODO creer la branche !
        
        return super(CreateBranchView, self).form_valid(form)