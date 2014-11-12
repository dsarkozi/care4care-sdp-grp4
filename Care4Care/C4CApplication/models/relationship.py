from django.db import models


class Relationship(models.Model):
    member = models.ForeignKey('Member')
    member = models.ForeignKey('Member')
    