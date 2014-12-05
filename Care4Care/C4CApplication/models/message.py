from django.db import models
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    member_sender = models.ForeignKey('Member')
    number = models.IntegerField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    
    TYPE = (
        (0, _('nothing')),
        (1, _('important')),
        (2, _('question')),
        (3, _('information')),
    )
    type = models.SmallIntegerField(choices=TYPE, default=0)
    date = models.DateField()   #'yyyy-mm-dd'
    
    class Meta:
        app_label = 'C4CApplication'
        unique_together = ('member_sender', 'number')