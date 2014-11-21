from time import strftime, gmtime


from django.db import models


class Member(models.Model): 
    
    mail = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    #picture = models.ImageField()
    birthday = models.DateField(default='2014-01-01')   #'yyyy-mm-dd'
    
    TAG_REVERSE = {
        1         : 'non_member',      #000001
        2         : 'member',          #000010
        4         : 'verified',        #000100
        8         : 'volunteer',       #001000
        16        : 'branch_officer',  #010000
        32        : 'bp_admin',        #100000
    }
    
    TAG = {
        'non_member'     : 1,   #000001
        'member'         : 2,   #000010
        'verified'       : 4,   #000100
        'volunteer'      : 8,   #001000
        'branch_officer' : 16,  #010000
        'bp_admin'       : 32,  #100000
    }
    tag = models.SmallIntegerField(default=1)    #Limit max
    status = models.BooleanField(default=True) # True = active, False = inactive
    mobile = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    register_date = models.DateField(default=strftime('%Y-%m-%d', gmtime()))
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
    #personal_network = models.ManyToManyField('Member', through='Relationship')

    def is_favorite(self, other_member):
        """
        :param other_member:
        :return: True if the email is in the favorite list of the member
        """

        for relation in self.relation.all():
            if relation.member == other_member:
                return True

        return False
    
    class Meta:
        app_label = 'C4CApplication'
