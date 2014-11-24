from django.views.generic.edit import FormView

from C4CApplication.models.member import Member
from C4CApplication.views.forms.BranchListForm import BranchListForm


class BranchListView(FormView):
    template_name = "C4CApplication/branchList.html"
    form_class = BranchListForm
    success_url = "home"
    member = None

    def get_context_data(self, **kwargs):
        context = super(BranchListView, self).get_context_data(**kwargs)

        # Get the personal list of the member
        # TODO test if the member has session variables !! -> redirection
        if BranchListView.member is None:
            BranchListView.member = Member.objects.get(mail=self.request.session['email'])

        branch_checked_name_list = []
        for branch in BranchListView.member.branch.all():
            branch_checked_name_list.append(branch.name)

        # Creates the form and change the context
        branch_list_form = BranchListForm(auto_id=False, initial={'branch_list': branch_checked_name_list})

        context['branch_list_form'] = branch_list_form
        return context

    def form_valid(self, form):
        # TODO test if the member has session variables !! -> redirection
        if BranchListView.member is None:
            BranchListView.member = Member.objects.get(mail=self.request.session['email'])

        branch_list = form.cleaned_data['branch_list']

        # Updates the list of the branches of the user
        BranchListView.member.branch = branch_list
        BranchListView.member.save()

        return super(BranchListView, self).form_valid(form)