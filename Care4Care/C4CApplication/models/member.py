from django.db import models


class Member(models.Model): 
    
    mail = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    #picture = models.ImageField()
    birthday = models.DateField()
    
    TAG = (
        (0, 'non_member'),
        (1, 'member'),
        (2, 'verified'),
        (3, 'volunteer'),
        (4, 'branch_officer'),
        (5, 'bp_admin'),
    )
    tag = models.SmallIntegerField(choices = TAG)
    status = models.BooleanField(default=True) # True = active, False = inactive
    mobile = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    register_date = models.DateField()
    dash_board_text = models.TextField()
    address = models.CharField(max_length=200)
    
    VISIBILITY = ( # every bit of the number corresponds to one option
        (1, 'anyone'), #0001
        (2, 'verified'), #0010
        (4, 'favorites'), #0100
        (8, 'network'), #1000
    )
    visibility = models.SmallIntegerField(choices = VISIBILITY, default=2)
    time_credit = models.BigIntegerField(default=0)
    
    branch = models.ManyToManyField('Branch')
    
    favorite = models.ForeignKey("self")
    #ignored = models.ForeignKey("self")
    
    #personal_network = models.ForeignKey(self)
    
    job = models.ManyToManyField('Job')
    
    class Meta:
        app_label = 'C4CApplication'
