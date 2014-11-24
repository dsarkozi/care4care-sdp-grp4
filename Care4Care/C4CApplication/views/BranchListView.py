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

        # Get the full list of branches
        branch_name_list = []
        for branch in Branch.objects.all():
            branch_name_list.append((branch.name, branch.name))
        branch_tuple = tuple(branch_name_list)

        # Get the personal list of the member
        member = Member.objects.get(mail="yves.deville@gmail.com")  # TODO get member from session variables !!

        branch_checked_name_list = []
        for branch in member.branch.all():
            branch_checked_name_list.append(branch.name)

        # Creates the form and change the context
        branch_list_form = BranchListForm(branch_tuple=branch_tuple, auto_id=False, initial={'weekdays':['0']})
        """for checkbox in branch_list_form['branchlist']:  # TODO
            if checkbox.choice_label in branch_checked_name_list:
                print('ok')
                checkbox.checked = True  # TODO change this line
            print(checkbox)"""


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