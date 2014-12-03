from django.views.generic import FormView
from C4CApplication import models
from C4CApplication.meta import Member, User
from C4CApplication.views.forms.TransferRightsBranchForm import TransferRightsBranchForm
from C4CApplication.views.utils import create_user

from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


class TransferRightsBranchView(FormView):
    template_name = "C4CApplication/TransferRightsBranch.html"
    form_class = TransferRightsBranchForm
    success_url = None
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])
        self.success_url = reverse_lazy("branchdetails", args=[self.kwargs['branch_name']])
        
        return super(TransferRightsBranchView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TransferRightsBranchView, self).get_context_data()
        context['member'] = self.user.db_member
        context['branch_name'] = self.kwargs['branch_name']
        context['form'] = self.get_form(self.get_form_class())
        return context

    def get_form_kwargs(self):
        kwargs = super(TransferRightsBranchView, self).get_form_kwargs()
        kwargs['auto_id'] = False
        return kwargs

    def form_valid(self, form):
        if TransferRightsBranchView.user is None:
            TransferRightsBranchView.user = models.Member.objects.get(mail=self.request.session['email'])

        # value entered in the input field
        email_new_branch_officer = form.cleaned_data['email_new_branch_officer']
        res = self.user.give_branch_control(self.kwargs['branch_name'], email_new_branch_officer)
        if not res:
            self.form_invalid(form)
            print("No such a member !")  # pop up ?
        
        return super(TransferRightsBranchView, self).form_valid(form)