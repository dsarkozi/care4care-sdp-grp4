from django.db import models


class Mailbox(models.Model):
    member = models.ForeignKey('Member')
    message = models.ForeignKey('Message')
    status = models.BooleanField(default=False) #False = notRead, True = read