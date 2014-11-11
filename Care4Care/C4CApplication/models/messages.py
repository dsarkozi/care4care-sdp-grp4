from django.db import models

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.EmailField(primary_key=True)
    subject = models.CharField(max_length=100)
    type = models.TextField()
    status = models.BooleanField()
    date = models.DateField()