from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    town = models.CharField(max_length=200)
    branch_officer = models.EmailField()
    address = models.CharField(max_length=200)
    
    # jobs = models.ForeignKey('Job') # TODO don't have to be in job instead ? 
    
    class Meta:
        app_label = 'C4CApplication'