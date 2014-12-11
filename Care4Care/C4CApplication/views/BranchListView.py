from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.core.exceptions import PermissionDenied

from C4CApplication.views.utils import create_user
from C4CApplication.models.member import Member
from C4CApplication.views.forms.BranchListForm import BranchListForm


class BranchListView(FormView):
    template_name = "C4CApplication/BranchList.html"
    form_class = BranchListForm
    success_url = reverse_lazy('myc4c')
    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(BranchListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BranchListView, self).get_context_data(**kwargs)

        self.user.db_member = Member.objects.get(mail=self.request.session['email'])

        branch_checked_name_list = []
        for branch in self.user.db_member.branch.all():
            branch_checked_name_list.append(branch.name)

        # Creates the form and change the context
        branch_list_form = BranchListForm(auto_id=False, initial={'branch_list': branch_checked_name_list})

        context['branch_list_form'] = branch_list_form
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session
        return context

    def form_valid(self, form):
        self.user.db_member = Member.objects.get(mail=self.request.session['email'])

        branch_list = form.cleaned_data['branch_list']

        # Updates the list of the branches of the user
        self.user.db_member.branch = branch_list
        self.user.db_member.save()

        return super(BranchListView, self).form_valid(form)