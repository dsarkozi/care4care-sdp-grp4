from django import forms


class BranchListForm(forms.Form):

    branch_tuple = ((0, 0), (1, 1))  # Default value

    weekdays = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={'disabled':'true'}
        ),
        choices=branch_tuple
    )

    def __init__(self, *args, **kwargs):
        if 'branch_tuple' in kwargs:
            BranchListForm.branch_tuple = kwargs.pop('branch_tuple')

        super(BranchListForm, self).__init__(args, kwargs)

        # List of checkbox
        self.fields['branchlist'] = forms.ChoiceField(choices=BranchListForm.branch_tuple,
                                                               widget=forms.CheckboxSelectMultiple())