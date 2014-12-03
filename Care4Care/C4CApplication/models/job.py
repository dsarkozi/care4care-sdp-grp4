from time import strftime, gmtime


from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    mail = models.EmailField()
    number = models.IntegerField()
    description = models.TextField()
    comment = models.CharField(max_length=200)
    date = models.DateField(default=strftime('%Y-%m-%d', gmtime()))
    start_time = models.IntegerField(default=0)
    
    FREQ = (
        (0, 'Once'),
        (1, 'Weekly'),
        (2, 'Monthly'),
    )
    frequency = models.SmallIntegerField(choices=FREQ, default=0)
    recursive_day = models.CharField(blank=True, max_length=150)
    km = models.SmallIntegerField(default=0)
    time = models.SmallIntegerField(default=0)
    
    CAT = (
        (1, 'Shopping'),
        (2, 'Visit'),
        (3, 'Transport'),
        (4, 'Other'),
    )
    CAT_DICT = {                #TODO Change this !
        1 : 'Shopping',
        2 : 'Visit',
        3 : 'Transport',
        4 : 'Other',
    }
    category = models.SmallIntegerField(choices=CAT)
    other_category = models.CharField(max_length=100)
    type = models.BooleanField(default=None) # True = demand, False = offer
    address = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    
    JOB_VISIBILITY_TUPLE = (
        (1, 'Anyone'),
        (2, 'Verified'),
        (4, 'Favorites'),
        (8, 'Network'),
        (16, 'Volunteer'),
    )
    
    JOB_VISIBILITY = { # every bit of the number corresponds to one option
        'anyone'     : 1,   #00001
        'verified'   : 2,   #00010
        'favorites'  : 4,   #00100
        'network'    : 8,   #01000
        'volunteer'  : 16,  #10000
    }
    visibility = models.SmallIntegerField(default=JOB_VISIBILITY['anyone'])
    branch = models.ForeignKey('Branch', blank=True, null=True)
    regular_job = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        app_label = 'C4CApplication'
        unique_together = ('mail', 'number')
