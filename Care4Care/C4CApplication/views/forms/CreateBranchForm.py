from django import forms
from django.forms.widgets import TextInput, EmailInput
from C4CApplication.models.branch import Branch


class CreateBranchForm(forms.Form):
    name = forms.CharField(
        widget=TextInput(
            attrs={'autofocus':'true', 'placeholder':'branch name'}
        ), label="Name of the branch "
    )
    
    branch_town = forms.CharField(
        widget=TextInput(
            attrs={'placeholder':'town(s) of the branch'}
        ), label="Name of the town "
    )
    
    branch_off = forms.EmailField(
        widget=EmailInput(
            attrs={'placeholder':'branch_officer@mail.com'}
        ), label="Branch officer mail"
    )
    
    street = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={'placeholder':'street, number, more details'}
        ),
        label="Street of the branch ",
    )
    
    zip = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={'placeholder':'postal code'}
        ),
        label="Zip of the branch ",
    )
    
    town = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={'placeholder':'town'}
        ),
        label="Town of the branch ",
    )
    
    def clean(self):
        """
        Overrides clean from super to add an error if 'other' has been checked,
        but nothing was provided in the text field.
        """
        cleaned_data = super(CreateBranchForm, self).clean()
        b_name = cleaned_data.get("name")
        list_branch = Branch.objects.filter(name=b_name)
        
        if len(list_branch) !=0 :
            self.add_error("name", forms.ValidationError("A branch already exist with this name.", code='invalid'))
            
        return cleaned_data
    