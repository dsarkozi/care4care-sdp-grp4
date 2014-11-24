from django.views.generic.edit import FormView

from C4CApplication.models.branch import Branch
from C4CApplication.models.member import Member
from C4CApplication.views.forms.BranchListForm import BranchListForm


class BranchListView(FormView):
    template_name = "C4CApplication/branchList.html"
    form_class = BranchListForm
    success_url = "branchlist"

    def get_context_data(self, **kwargs):
        context = super(BranchListView, self).get_context_data(**kwargs)

        # Get the personal list of the member
        member = Member.objects.get(mail="yves.deville@gmail.com")  # TODO get member from session variables !!

        branch_checked_name_list = []
        for branch in member.branch.all():
            branch_checked_name_list.append(branch.name)

        # Creates the form and change the context
        branch_list_form = BranchListForm(auto_id=False, initial={'branch_list': branch_checked_name_list})

        context['branch_list_form'] = branch_list_form
        return context

    def form_valid(self, form):
        branch_list = form.cleaned_data['branchlist']
        print(branch_list)
        #TODO change user data
        return super(BranchListView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        #TODO change user data
        pass