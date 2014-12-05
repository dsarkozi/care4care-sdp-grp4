import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple, PasswordInput
from localflavor.be.forms import BEPostalCodeField
from C4CApplication.models.branch import Branch
from C4CApplication.models.member import Member
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(ModelForm):
    class Meta:
        model = Member
        fields = (
            'mail',
            'password',
            'first_name',
            'last_name',
            'gender',
            'picture',
            'birthday',
            'mobile',
            'telephone',
            'street',
            'town',
            'branch',
            'zip',
        )
        labels = {
            'mail' : _('E-mail address'),
            'street' : _('Street'),
            'town' : _('City'),
            'password' : _('password'),
            'first_name' : _('first name'),
            'last_name' : _('last name'),
            'gender' : _('gender'),
            'picture' : _('picture'),
            'birthday' : _('birthday'),
            'mobile' : _('mobile'),
            'telephone' : _('telephone'),
            'branch' : _('branch')
            
            
        }
        widgets = {
            'branch' : CheckboxSelectMultiple(),
            'password' : PasswordInput(),
            'birthday' : SelectDateWidget(years=range(1900, 2050)),         #TODO Change this to more dynamic values
        }


    def __init__(self, *args, **kwargs):
        eid = kwargs.pop('eid')
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.all()
        self.fields['birthday'].initial = datetime.date.today()
        self.fields['zip'] = BEPostalCodeField(label = _('Postal code'))

        self.auto_id = False
        if eid:
            self.fields['first_name'].widget.attrs.update({'disabled' : 'true'})
            self.fields['last_name'].widget.attrs.update({'disabled' : 'true'})
            self.fields['street'].widget.attrs.update({'disabled' : 'true'})
            self.fields['zip'].widget.attrs.update({'disabled' : 'true'})
            self.fields['town'].widget.attrs.update({'disabled' : 'true'})
            self.fields['birthday'].widget.attrs.update({'disabled' : 'true'})

        self.fields['tag'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=((1, _("Without time crediting")), (2, _("With time crediting"))),
            label=_("Account type")
        )
        self.fields['gender'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=(('M', 'M'), ('F', 'F') ), label = _('gender'))
        