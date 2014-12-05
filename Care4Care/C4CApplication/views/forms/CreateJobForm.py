from django import forms
from django.forms.widgets import TextInput
from django.forms.extras.widgets import SelectDateWidget

from C4CApplication.models.job import Job


class CreateJobForm(forms.ModelForm):
    #TODO Put some magical js for disabled fields toggle

    class Meta:
        model = Job
        fields = (
            'title',
            'description',
            'category',
            'frequency',
            'visibility',
            'date',
            'km',
            'start_time'
        )
        labels = {
        }
        widgets = {
            'description' : forms.Textarea(
                attrs = {'id':'job_desc', 'rows':3, 'placeholder':'Request description'}
            ),
            'date' : SelectDateWidget(attrs={'id':'time_specific', }),   #TODO disabled
        }

    class HTML5TimeInput(forms.TimeInput):
        input_type = 'time'

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
            choices=tuple(branchList)
        )
        if branchAmount == 1:
            self.fields['branches'].widget.attrs = {'disabled' : 'true', 'checked' : 'true'}
        self.fields['title'].widget.attrs = {'autofocus':'true', 'id':'job_title', 'placeholder':'Request title'}
        self.fields['start_time'] = forms.TimeField(
            widget=self.HTML5TimeInput,
            label='Start time'
        )
        self.fields['km'] = forms.DecimalField(
            min_value=0,
            initial=0,
            label='Distance to be covered (approximation)',
            max_digits=4,
        )

        # Job category fieldset
        self.fields['category'] = forms.MultipleChoiceField(
            widget=forms.RadioSelect,
            choices=Job.CAT
        )
        self.fields['other'] = forms.CharField(
            required=False,
            widget=TextInput(
                attrs={'placeholder':'Other'}    #TODO disabled
            )
        )

        # Job visibility fieldset
        self.fields['visibility'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=Job.JOB_VISIBILITY_TUPLE
        )
        self.fields['frequency'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=Job.FREQ
        )




    # Job timeline fieldset
    subfrequency = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={}   #TODO disabled
        ),
        choices=(('specific','Specific day'), ('weekday','Weekdays')),
    )
    WEEKDAYS = (
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
        ('sunday','Sunday')
    )
    weekdays = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={}    #TODO disabled
        ),
        choices=WEEKDAYS
    )
    DAYPARTS = (
        ('morning','Morning'),
        ('afternoon','Afternoon'),
        ('evening','Evening'),
        ('any','Anytime')
    )
    dayparts = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={}   #TODO disabled
        ),
        choices=DAYPARTS
    )


    def clean(self):
        """
        Overrides clean from super to add an error if 'other' has been checked,
        but nothing was provided in the text field.
        """
        #TODO Verify if further validations are needed for the nested selectors
        
        cleaned_data = super(CreateJobForm, self).clean()
        category = cleaned_data.get("categories")
        other = cleaned_data.get("other")
        if category == 'other' and other == '':
            self.add_error("other", forms.ValidationError("If other is checked, fill the text input in.", code='missing'))
        return cleaned_data