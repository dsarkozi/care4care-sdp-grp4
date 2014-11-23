from time import strftime, gmtime


from django.db import models


class Job(models.Model):
    mail = models.EmailField()
    number = models.IntegerField()
    comment = models.CharField(max_length=200)
    date = models.DateField(default=strftime('%Y-%m-%d', gmtime()))
    start_time = models.IntegerField(default=0)
    
    FREQ = (
        (0, 'once'),
        (1, 'daily'),
        (2, 'weekly'),
        (3, 'monthly'),
        (4, 'yearly'),
    )
    frequency = models.SmallIntegerField(choices=FREQ, default=0)
    km = models.SmallIntegerField(default=0)
    time = models.SmallIntegerField(default=0)
    
    CAT = (
        (1, 'shopping'),
        (2, 'visit'),
        (3, 'transport'),
    )
    category = models.SmallIntegerField(choices=CAT)
    type = models.BooleanField(default=None) # True = demand, False = offer
    address = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    
    JOB_VISIBILITY = { # every bit of the number corresponds to one option
        'anyone'     : 1,   #00001
        'verified'   : 2,   #00010
        'favorites'  : 4,   #00100
        'network'    : 8,   #01000
        'volunteer'  : 16,  #10000
    }
    visibility = models.SmallIntegerField(default=JOB_VISIBILITY['anyone'])
    branch = models.ForeignKey('Branch')
    
    class Meta:
        app_label = 'C4CApplication'
        unique_together = ('mail', 'number')
