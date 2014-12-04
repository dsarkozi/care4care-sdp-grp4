from django import forms

from C4CApplication.models.branch import Branch


class BranchListForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(BranchListForm, self).__init__(*args, **kwargs)
        
        branch_name_list = []
        for branch in Branch.objects.all():
            branch_name_list.append((branch.name, branch.name))
        branch_tuple = tuple(branch_name_list)
        
        self.fields['branch_list'] = forms.MultipleChoiceField(choices=branch_tuple,
                                                               widget=forms.CheckboxSelectMultiple(),)