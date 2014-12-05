from django import forms
from C4CApplication.models.member import Member
from django.utils.translation import ugettext_lazy as _


class DonateTimeForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':'5'}
        )
    )
    days = forms.DecimalField(
        initial = 0,
        min_value=0,
    )
    hours = forms.DecimalField(
        initial = 0,
        min_value=0,
    )
    minutes = forms.DecimalField(
        initial = 0,
        min_value=0,
    )
    receiver = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(('c4c', _('Send to one of your branches')), ('user', _('Send to user')))
    )
    userDropdown = forms.ChoiceField(
        widget=forms.Select,
        choices=Member.objects.values_list('mail',_('first_name'))
    )
    
    
    def __init__(self, db_member=None, *args, **kwargs):
        super(DonateTimeForm, self).__init__(*args, **kwargs)
        
        BRANCH = ()
        if db_member is not None:
            for branch in db_member.branch.all():
                BRANCH += ((branch.name,branch.name),)
        
        self.fields['branchDropdown'] = forms.CharField(widget=forms.Select(choices=BRANCH))
        
    def clean(self):
        cleaned_data = super(DonateTimeForm, self).clean()
        time = 0
        days = 0
        days = cleaned_data.get(_("days"))
        hours = 0
        hours = cleaned_data.get(_("hours"))
        minutes = 0
        minutes = cleaned_data.get(_("minutes"))
        time = days*1440+hours*60+minutes
        
        #check a good time donation
        if time == 0 :
            self.add_error(_("minutes"), forms.ValidationError(_("You can't do a donation of 0 time !"), code='invalid'))
        
        return cleaned_data