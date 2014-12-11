from django.views.generic import FormView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy

from C4CApplication import models
from C4CApplication.views.forms.CreateBranchForm import CreateBranchForm
from C4CApplication.views.utils import create_user


class CreateBranchView(FormView):
    template_name = "C4CApplication/CreateBranch.html"
    form_class = CreateBranchForm
    success_url = reverse_lazy("profile")
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
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session

        context['create_branch_form'] = create_branch_form
        return context

    def form_valid(self, form):
        if self.user is None:
            self.user = models.Member.objects.get(mail=self.request.session['email'])

        # create the branch with the values entered in the input field
        res = self.user.create_branch(form.cleaned_data['name'], form.cleaned_data['branch_town'],\
                                form.cleaned_data['branch_off'], form.cleaned_data['street'],\
                                form.cleaned_data['zip'], form.cleaned_data['town'])

        
        return super(CreateBranchView, self).form_valid(form)