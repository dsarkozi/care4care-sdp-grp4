from django import forms


class MultipleChoiceFieldWithInitialValues(forms.MultipleChoiceField):


    def __init__(self, checked_list, *args, **kwargs):
        super(MultipleChoiceFieldWithInitialValues, self).__init__(args, kwargs)
        self.checked_list = checked_list

    def render(self):
        super(MultipleChoiceFieldWithInitialValues, self)



class BranchListForm(forms.Form):

    branch_tuple = tuple([(0, 0), (1, 1)])  # Default value

    def __init__(self, *args, **kwargs):
        if 'branch_tuple' in kwargs:
            BranchListForm.branch_tuple = kwargs.pop('branch_tuple')

        super(BranchListForm, self).__init__(args, kwargs)

        # List of checkbox
        self.fields['branch_list'] = forms.MultipleChoiceField(choices=BranchListForm.branch_tuple,
                                                               widget=forms.CheckboxSelectMultiple(),
                                                               initial=['LLN'])