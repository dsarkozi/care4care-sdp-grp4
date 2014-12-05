from time import strftime, gmtime


from django.db import models
from localflavor.be.forms import BEPostalCodeField


class Job(models.Model):
    title = models.CharField(max_length=100)
    mail = models.EmailField()
    number = models.IntegerField()
    description = models.TextField()
    comment = models.CharField(blank=True, max_length=200)
    date = models.DateField(null=True)
    start_time = models.IntegerField(null=True, blank=True)
    
    FREQ = (
        (0, 'Once'),
        (1, 'Weekly'),
        (2, 'Monthly'),
    )
    frequency = models.SmallIntegerField(choices=FREQ)
    recursive_day = models.CharField(blank=True, max_length=150)
    km = models.SmallIntegerField(blank=True, default=0)
    duration = models.SmallIntegerField()
    
    CAT = (
        (1, 'Shopping'),
        (2, 'Visit'),
        (3, 'Transport'),
        (4, 'Other'),
    )
    CAT_DICT = {
        1 : 'Shopping',
        2 : 'Visit',
        3 : 'Transport',
        4 : 'Other',
    }
    category = models.SmallIntegerField(choices=CAT)
    other_category = models.CharField(blank=True, max_length=100)
    type = models.BooleanField(default=None) # True = demand, False = offer
    place = models.TextField(blank=True)
    accepted = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    
    JOB_VISIBILITY_TUPLE = (
        (1, 'Anyone'),
        (2, 'Verified'),
        (4, 'Favorites'),
        (8, 'Volunteer'),
    )
    
    JOB_VISIBILITY = { # every bit of the number corresponds to one option
        'anyone'     : 1,   #0001
        'verified'   : 2,   #0010
        'favorites'  : 4,   #0100
        'volunteer'  : 8,   #1000
    }
    visibility = models.SmallIntegerField(default=JOB_VISIBILITY['verified'])
    branch = models.ForeignKey('Branch')
    regular_job = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        app_label = 'C4CApplication'
        unique_together = ('mail', 'number')
