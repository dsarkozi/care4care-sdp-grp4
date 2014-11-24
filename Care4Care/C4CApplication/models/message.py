from django.db import models


class Message(models.Model):
    member_sender = models.ForeignKey('Member')
    number = models.IntegerField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    
    TYPE = (
        (0, 'nothing'),
        (1, 'important'),
        (2, 'question'),
        (3, 'information'),
    )
    type = models.SmallIntegerField(choices=TYPE, default=0)
    date = models.DateField()   #'yyyy-mm-dd'
    
    class Meta:
        app_label = 'C4CApplication'
        unique_together = ('member_sender', 'number')