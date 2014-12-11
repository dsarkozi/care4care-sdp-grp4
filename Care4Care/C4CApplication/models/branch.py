from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    branch_town = models.CharField(max_length=200)
    branch_officer = models.EmailField()
    street = models.CharField(blank=True, max_length=200)   #Street and number
    zip = models.CharField(blank=True, max_length=4)
    town = models.CharField(blank=True, max_length=100)
    donation = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'C4CApplication'