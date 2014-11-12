from django.db import models


class Mailbox(models.Model):
    member = models.ForeignKey('Member')
    message = models.ForeignKey('Message')
    