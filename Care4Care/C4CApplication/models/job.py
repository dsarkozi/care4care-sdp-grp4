from django.db import models


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.EmailField(primary_key=True)
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
    frequence = models.SmallIntegerField(choices=FREQ)
    km = models.SmallIntegerField()
    time = models.SmallIntegerField()
    
    CAT = (
        (1, 'shopping'),
        (2, 'visit'),
        (3, 'transport'),
    )
    job_category = models.SmallIntegerField(choices=CAT)
    type = models.BooleanField(default=None) # True = demand, False = offer
    adresse = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)
    
    class Meta:
        app_label = 'C4CApplication'
