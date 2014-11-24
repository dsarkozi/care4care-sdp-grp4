from django import forms

from C4CApplication.models.branch import Branch


class BranchListForm(forms.Form):

    branch_name_list = []
    for branch in Branch.objects.all():
        branch_name_list.append((branch.name, branch.name))
    branch_tuple = tuple(branch_name_list)

    branch_list = forms.ChoiceField(choices=branch_tuple,
                                    widget=forms.CheckboxSelectMultiple())