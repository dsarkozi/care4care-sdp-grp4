from time import strftime, gmtime


from django.db import models


class Member(models.Model): 
    
    mail = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    '''def upload_path(self):
        return 'C4CApplication/static/images/images_profile/%s_picture' % (self.mail)'''
    picture = models.ImageField(upload_to="images/images_profile/")
    birthday = models.DateField(default='2014-01-01')   #'yyyy-mm-dd'
    
    TAG_REVERSE = {
        1         : 'non_member',      #000001
        2         : 'member',          #000010
        4         : 'verified',        #000100
        8         : 'volunteer',       #001000
        16        : 'branch_officer',  #010000
        32        : 'bp_admin',        #100000
    }
    
    TAG_CHOICE = (
        (1, 'Non_member'),
        (2, 'Member'),
        (4, 'Verified'),
        (8, 'Volunteer'),
        (16, 'Branch_officer'),
        (32, 'BP_admin'),
    )
    
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
    deleted = models.BooleanField(default=False)
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
    relation = models.ManyToManyField('self', through='Relationship', symmetrical=False)
    job = models.ManyToManyField('Job')
    #personal_network = models.ManyToManyField('Member', through='Relationship')
    
    def __unicode__(self):
            return unicode(self.first_name)

    def is_favorite(self, other_member): 
        """
        :param other_member:
        :return: True if the email is in the favorite list of the member
        """
        for relation in self.relation.all():
            if relation == other_member: #TODO this line won't work
                return True
        return False
    
    class Meta:
        app_label = 'C4CApplication'
