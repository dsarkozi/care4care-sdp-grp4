from django.db import models


class Job(models.Model):
    #id = models.AutoField(primary_key=True)
    #mail = models.EmailField(primary_key=True)
    mail = models.EmailField()
    done = models.BooleanField(default=False)
    comment = models.CharField(max_length=200)
    start_time = models.IntegerField()
    
    FREQ = (
        (0, 'once'),
        (1, 'daily'),
        (2, 'weekly'),
        (3, 'monthly'),
        (4, 'yearly'),
    )
    frequency = models.SmallIntegerField(choices=FREQ)
    km = models.SmallIntegerField(default=0)
    time = models.SmallIntegerField()
    
    CAT = (
        (1, 'shopping'),
        (2, 'visit'),
        (3, 'transport'),
    )
    job_category = models.SmallIntegerField(choices=CAT)
    type = models.BooleanField(default=None) # True = demand, False = offer
    address = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)
    branch = models.ForeignKey('Branch')
    
    class Meta:
        app_label = 'C4CApplication'
