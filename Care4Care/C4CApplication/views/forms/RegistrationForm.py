import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple, PasswordInput
from C4CApplication.models.branch import Branch
from C4CApplication.models.member import Member


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
            'zip',
            'branch',
        )
        labels = {
            'mail' : 'E-mail address',
            'street' : 'Street',
            'town' : 'City',
            'zip' : 'Postal code'
        }


    def __init__(self, *args, **kwargs):
        eid = kwargs.pop('eid')
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['branch'].widget = CheckboxSelectMultiple()
        self.fields['branch'].queryset = Branch.objects.all()

        self.fields['password'].widget = PasswordInput()

        self.fields['birthday'].widget = SelectDateWidget(
            years=range(1900, 2050),        #TODO Change this to more dynamic values
        )
        self.fields['birthday'].initial = datetime.date.today()

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
            choices=((1, "Without time crediting"), (2, "With time crediting")),
            label="Account type"
        )
        self.fields['gender'].widget = forms.RadioSelect
        self.fields['gender'].choices = (('M', 'M'), ('F', 'F'))