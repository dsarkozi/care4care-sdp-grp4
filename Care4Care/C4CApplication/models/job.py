from django.db import models

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.EmailField(primary_key=True)
    done = models.BooleanField()
    comment = models.CharField(max_length=200)
    start_time = models.IntegerField()
    frequence = models.SmallIntegerField()
    km = models.SmallIntegerField()
    time = models.SmallIntegerField()
    job_category = models.SmallIntegerField()
    type = models.BooleanField()
    adresse = models.CharField(max_length=200)