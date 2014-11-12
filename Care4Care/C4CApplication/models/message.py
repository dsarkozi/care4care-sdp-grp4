from django.db import models


class Message(models.Model):
    mail = models.EmailField()
    number = models.IntegerField()
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
    
    member = models.ForeignKey('Message')
    
    class Meta:
        app_label = 'C4CApplication'
        unique_together = ('mail', 'number')