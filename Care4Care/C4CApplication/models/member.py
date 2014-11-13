from django.db import models


class Member(models.Model): 
    
    mail = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    #picture = models.ImageField()
    birthday = models.DateField()   #'yyyy-mm-dd'
    
    TAG = {
        'non_member'     : 1,   #000001
        'member'         : 2,   #000010
        'verified'       : 4,   #000100
        'volunteer'      : 8,   #001000
        'branch_officer' : 16,  #010000
        'bp_admin'       : 32,  #100000
    }
    tag = models.SmallIntegerField()    #Limit max
    status = models.BooleanField(default=True) # True = active, False = inactive
    mobile = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    register_date = models.DateField()
    dash_board_text = models.TextField()
    address = models.CharField(max_length=200)
    
    MEMBER_VISIBILITY = { # every bit of the number corresponds to one option
        'anyone'     : 1,   #0001
        'verified'   : 2,   #0010
        'favorites'  : 4,   #0100
        'network'    : 8,   #1000
    }
    visibility = models.SmallIntegerField(default=MEMBER_VISIBILITY['verified'])
    time_credit = models.BigIntegerField(default=0)
    
    branch = models.ManyToManyField('Branch')
    message = models.ManyToManyField('Message', through='Mailbox')
    relation = models.ManyToManyField('Member', through='Relationship')
    job = models.ManyToManyField('Job')
    #personal_network = models.ForeignKey(self)
    
    class Meta:
        app_label = 'C4CApplication'
