from django import forms
from django.forms.widgets import TextInput
from django.forms.extras.widgets import SelectDateWidget
from django.http.request import QueryDict

from C4CApplication.models.job import Job
from django.utils.translation import ugettext_lazy as _


class CreateJobForm(forms.ModelForm):
    #TODO Put some magical js for disabled fields toggle

    class Meta:
        model = Job
        fields = (
            'title',
            'description',
            'category',
            'other_category',
            'frequency',
            'visibility',
            'date',
            'km',
            'place',
        )
        labels = {
        }
        widgets = {
            'description' : forms.Textarea(
                attrs = {'id':'job_desc', 'rows':3, 'placeholder':_('Request description')}
            ),
            'place' : forms.Textarea(
                attrs = {'rows':3, 'placeholder':_('Location details')}
            ),
            'date' : SelectDateWidget(attrs={'id':'time_specific', }),   #TODO disabled
            'other_category' : forms.TextInput(attrs={'placeholder' : _('Specify')})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreateJobForm, self).__init__(*args, **kwargs)

        # Request details fieldset
        branchList = []
        for branch in user.branch.all():
            branchList.append((branch.name, branch.name))
        branchAmount = len(branchList)
        self.fields['branches'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=tuple(branchList),
        )
        if branchAmount == 1:
            data = QueryDict('', mutable=True)
            data.update(self.data)
            data['branches'] = branchList[0][0]
            self.data = data
            self.fields['branches'].widget.attrs = {'disabled' : 'true', 'checked' : 'true'}
        self.fields['title'].widget.attrs = {'autofocus':'true', 'id':'job_title', 'placeholder':_('Request title')}
        self.fields['date'].required = False
        self.fields['start_time'] = forms.TimeField(
            widget=forms.TimeInput(
                attrs={'placeholder' : 'Format: 00:00'},
            ),
            label='Start time',
        )
        self.fields['duration'] = forms.TimeField(
            widget=forms.TimeInput(
                attrs={'placeholder' : 'Format: 00:00'},
            ),
            label='Duration',
        )
        self.fields['km'] = forms.DecimalField(
            min_value=0,
            initial=0,
            label='Distance to be covered (approximation)',
            max_digits=4,
        )

        # Job category fieldset
        self.fields['category'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=Job.CAT
        )
        # self.fields['other'] = forms.CharField(
        #     required=False,
        #     widget=TextInput(
        #         attrs={'placeholder':'Other'}    #TODO disabled
        #     )
        # )

        # Job timeline fieldset
        self.fields['frequency'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=Job.FREQ
        )
        self.fields['dayrange'] = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=((x,x) for x in range(1,32))
        )

        # Job visibility fieldset
        self.fields['visibility'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=Job.JOB_VISIBILITY_TUPLE
        )





    # Job timeline fieldset
    # subfrequency = forms.ChoiceField(
    #     widget=forms.RadioSelect(
    #         attrs={}   #TODO disabled
    #     ),
    #     choices=(('specific','Specific day'), ('weekday','Weekdays')),
    # )
    WEEKDAYS = (
        (0,_('Monday')),
        (1,_('Tuesday')),
        (2,_('Wednesday')),
        (3,_('Thursday')),
        (4,_('Friday')),
        (5,_('Saturday')),
        (6,_('Sunday'))
    )
    weekdays = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={}    #TODO disabled
        ),
        choices=WEEKDAYS
    )
    # DAYPARTS = (
    #     ('morning','Morning'),
    #     ('afternoon','Afternoon'),
    #     ('evening','Evening'),
    #     ('any','Anytime')
    # )
    # dayparts = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple(
    #         attrs={}   #TODO disabled
    #     ),
    #     choices=DAYPARTS
    # )


    def clean_visibility(self):
        """
        Cleans the visibility field by converting the choices from a list of strings to a sum of integers.
        """
        visibility = self.cleaned_data['visibility']
        res = 0
        for vis in visibility:
            res += int(vis)
        return res

    def clean(self):
        """
        Overrides clean from super to add an error if 'other' has been checked,
        but nothing was provided in the text field.
        """
        #TODO Verify if further validations are needed for the nested selectors

        cleaned_data = super(CreateJobForm, self).clean()
        # Other category
        category = cleaned_data.get("category")
        other = cleaned_data.get("other_category")
        if category == '4' and other == '':
            self.add_error("category", forms.ValidationError("If other is checked, fill the text input in.", code='missing'))

        # Frequency
        frequency = cleaned_data.get("frequency")
        if frequency is not None:
            if int(frequency) != 0:
                cleaned_data.update({'date' : None})
            if int(frequency) == 1 and not cleaned_data.get("weekdays"):
                self.add_error("frequency", forms.ValidationError("Please provide at least one weekday.", code='missing'))
            elif int(frequency) == 2 and not cleaned_data.get("dayrange"):
                self.add_error("frequency", forms.ValidationError("Please provide at least one day.", code='missing'))
        return cleaned_data