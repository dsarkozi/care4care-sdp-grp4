from django.db import models

class Member(models.Model): 
    mail = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField()
    birthday = models.DateField()
    tag = models.SmallIntegerField()
    status = models.BooleanField()
    mobile = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    register_date = models.DateField()
    dash_board_text = models.TextField()
    adresse = models.CharField(max_length=200)
    visibility = models.SmallIntegerField()
    time_credit = models.BigIntegerField()
    accepted = models.BooleanField()
    
    