from django.db import models


class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.EmailField(primary_key=True)
    subject = models.CharField(max_length=100)
    
    TYPE = (
        (0, 'nothing'),
        (1, 'important'),
        (2, 'question'),
        (3, 'information'),
    )
    type = models.SmallIntegerField(choices = TYPE, default=0)
    status = models.BooleanField(default=False) #False = notRead, True = read
    date = models.DateField()