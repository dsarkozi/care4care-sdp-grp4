from django import forms
from django.forms.widgets import TextInput, Textarea
from django.forms.extras.widgets import SelectDateWidget

from C4CApplication.models.job import Job


class CreateJobForm(forms.Form):
    #TODO Put some magical js for disabled fields toggle

    # Request details fieldset
    title = forms.CharField(
        widget=TextInput(
            attrs={'autofocus':'true', 'id':'job_title', 'placeholder':'Request title'}
        )
    )
    desc = forms.CharField(
        widget=Textarea(
            attrs={'id':'job_desc', 'rows':3, 'placeholder':'Request description'}
        )
    )

    # Job category fieldset
    categories = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Job.CAT
    )
    other = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={'placeholder':'Other', 'disabled':'true'}
        )
    )
    categories.choices.extend([('other','other')])

    # Job timeline fieldset
    frequency = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(('once', 'Only once'), ('regular', 'Regularly'))
    )
    subfrequency = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={'disabled':'true'}
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
    weekdays = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={'disabled':'true'}
        ),
        choices=WEEKDAYS
    )
    DAYPARTS = (
        ('morning','Morning'),
        ('afternoon','Afternoon'),
        ('evening','Evening'),
        ('any','Anytime')
    )
    dayparts = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={'disabled':'true'}
        ),
        choices=DAYPARTS
    )
    specific = forms.ChoiceField(
        widget=SelectDateWidget(
            attrs={'id':'time_specific', 'disabled':'true'}
        )
    )

    # Job visibility fieldset
    VISIBILITY = (
        ('any', 'Anyone'),
        ('verified', 'Verified members only'),
        ('favorites', 'My favorites only'),
        ('personal', 'My personal network only'),
        ('default', 'Apply my default preferences')     # TODO Gather from database
    )
    visibility = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=VISIBILITY
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