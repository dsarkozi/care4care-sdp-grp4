from django.db import models
#from django.db.models.fields.related import ForeignKey

class Member(models.Model): 
    mail = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField()
    birthday = models.DateField()
    TAG = (
        (0, 'non_member'),
        (1, 'member'),
        (2, 'verified'),
        (3, 'volonteer'),
        (4, 'branch_off'),
        (5, 'bp_admin'),
    )
    
    tag = models.SmallIntegerField(choices = TAG)
    status = models.BooleanField()
    mobile = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    register_date = models.DateField()
    dash_board_text = models.TextField()
    adresse = models.CharField(max_length=200)
    
    VISIBILITY = (
        (0, 'anyone'),
        (1, 'verified'),
        (2, 'favorites'),
        (3, 'network'),
    )
    visibility = models.SmallIntegerField(choices = VISIBILITY)
    time_credit = models.BigIntegerField()
    accepted = models.BooleanField()
    
    branch = models.ManyToManyField('Branch')
    favorite = models.ForeignKey("self")
    ignored = models.ForeignKey("self")
    #personal_network = models.ForeignKey(self)
    job = models.ManyToManyField('Job')
    message = models.ManyToManyField('Message')
    