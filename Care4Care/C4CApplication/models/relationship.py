from django.db import models


class Relationship(models.Model):
    member = models.ForeignKey('Member')
    member = models.ForeignKey('Member')
    #favorite = models.BooleanField(default=True) #False = notRead, True = read