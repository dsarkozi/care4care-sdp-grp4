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
            'password' : _('Password'),
            'first_name' : _('First name'),
            'last_name' : _('Last name'),
            'gender' : _('Gender'),
            'birthday' : _('Birthday'),
            'mobile' : _('Mobile number'),
            'telephone' : _('Phone number'),
            'branch' : _('Branch')
        }
        widgets = {
            'branch' : CheckboxSelectMultiple(),
            'password' : PasswordInput(),
            'birthday' : SelectDateWidget(years=range(1900, 2050)),
        }

    eid = False

    def __init__(self, *args, **kwargs):
        self.eid = kwargs.pop('eid')
        # Prevents from validating empty form after eID request
        if self.eid:
            kwargs['empty_permitted'] = True
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'] = forms.CharField(
            max_length=100,
            min_length=8,
            widget=PasswordInput(),
            label=_('Password')
        )
        self.fields['confirm'] = forms.CharField(
            max_length=100,
            min_length=8,
            widget=PasswordInput(),
            label=_('Confirm password')
        )
        self.fields['picture'] = forms.ImageField(required=False, label=_('Picture'))
        self.fields['branch'].queryset = Branch.objects.all()
        self.fields['birthday'].initial = datetime.date.today()
        self.fields['zip'] = BEPostalCodeField(label = _('Postal code'))

        self.fields['tag'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=((1, _("Without time crediting")), (2, _("With time crediting"))),
            label=_("Account type")
        )
        self.fields['gender'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=(('M', 'M'), ('F', 'F') ))

        self.auto_id = False
        if self.eid:
            if kwargs['data']['first_name']: self.fields['first_name'].widget.attrs.update({'disabled' : 'true'})
            if kwargs['data']['last_name']: self.fields['last_name'].widget.attrs.update({'disabled' : 'true'})
            if kwargs['data']['street']: self.fields['street'].widget.attrs.update({'disabled' : 'true'})
            if kwargs['data']['zip']: self.fields['zip'].widget.attrs.update({'disabled' : 'true'})
            if kwargs['data']['town']: self.fields['town'].widget.attrs.update({'disabled' : 'true'})
            if kwargs['data']['birthday_day'] and kwargs['data']['birthday_month'] and kwargs['data']['birthday_year']:
                self.fields['birthday'].widget.attrs.update({'disabled' : 'true'})
            if kwargs['data']['gender']: self.fields['gender'].widget.attrs.update({'disabled' : 'true'})

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm")
        if password != confirm:
            self.add_error('password', forms.ValidationError(_("The password and confirmation do not match."), code='invalid'))
        return cleaned_data
