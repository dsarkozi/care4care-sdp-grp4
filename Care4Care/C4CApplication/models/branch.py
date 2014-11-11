from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    town = models.CharField(max_length=200)
    branch_officer = models.EmailField()
    adress = models.CharField(max_length=200)
    
    jobs = models.ForeignKey('Job')