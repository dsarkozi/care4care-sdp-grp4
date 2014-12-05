from django import forms
from django.forms.widgets import TextInput, EmailInput
from C4CApplication.models.branch import Branch
from django.utils.translation import ugettext_lazy as _


class CreateBranchForm(forms.Form):
    name = forms.CharField(
        widget=TextInput(
            attrs={'autofocus':'true', 'placeholder':_("branch name")}
        ), label= _("Name of the branch ")
    )
    
    branch_town = forms.CharField(
        widget=TextInput(
            attrs={'placeholder':_('town(s) of the branch')}
        ), label=_("Name of the town ")
    )
    
    branch_off = forms.EmailField(
        widget=EmailInput(
            attrs={'placeholder':_('branch_officer@mail.com')}
        ), label=_("Branch officer mail")
    )
    
    street = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={'placeholder':_('street, number, more details')}
        ),
        label=_("Street of the branch "),
    )
    
    zip = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={'placeholder':_('postal code')}
        ),
        label=_("Zip of the branch "),
    )
    
    town = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={'placeholder':_('town')}
        ),
        label=_("Town of the branch "),
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
            self.add_error("name", forms.ValidationError(_("A branch already exist with this name."), code='invalid'))
            
        return cleaned_data
    