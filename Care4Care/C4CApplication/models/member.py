from time import strftime, gmtime

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        if self.exists(name):
            self.delete(name)
        return name


class Member(models.Model):
    mail = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    eid = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    picture = models.ImageField(null=True, blank=True, upload_to="images/images_profile/", storage=OverwriteStorage())
    birthday = models.DateField(blank=True, null=True)   #'yyyy-mm-dd'   
    
    TAG_REVERSE = {
        1         : _('non_member'),               #000001
        2         : _('member'),                   #000010
        4         : _('verified'),                 #000100
        8         : _('volunteer'),                #001000
        16        : _('branch_officer'),           #010000
        32        : _('bp_admin'),                 #100000
    }
    
    TAG_CHOICE = (
        (1, _('Non member')),
        (2, _('Member')),
        (4, _('Verified')),
        (8, _('Volunteer')),
        (16, _('Branch officer')),
        (32, _('BP admin')),
    )
    
    TAG = {
        'non_member'            : 1,   #000001
        'member'                 : 2,   #000010
        'verified'               : 4,   #000100
        'volunteer'              : 8,   #001000
        'branch_officer'         : 16,  #010000
        'bp_admin'               : 32,  #100000
    }
    tag = models.SmallIntegerField()    #Limit max
    status = models.BooleanField(default=True) # True = active, False = inactive
    deleted = models.BooleanField(default=False)
    mobile = models.CharField(blank=True, max_length=15)
    telephone = models.CharField(blank=True, max_length=15)
    register_date = models.DateField(default=strftime('%Y-%m-%d', gmtime()))
    street = models.CharField(max_length=200)   #Street and number
    zip = models.CharField(max_length=4)
    town = models.CharField(max_length=100)
    
    MEMBER_VISIBILITY_TUPLE = (
        (1, 'Anyone'),
        (2, 'Verified'),
        (4, 'Favorites'),
        (8, 'Volunteer'),
    )
    
    MEMBER_VISIBILITY = { # every bit of the number corresponds to one option
        'anyone'     : 1,   #001
        'verified'   : 2,   #010
        'favorites'  : 4,   #100
    }
    visibility = models.SmallIntegerField(default=MEMBER_VISIBILITY['verified'])
    time_credit = models.BigIntegerField(default=0)
    
    branch = models.ManyToManyField('Branch')
    relation = models.ManyToManyField('self', through='Relationship', symmetrical=False, blank=True, null=True)
    job = models.ManyToManyField('Job', blank=True, null=True)
    #personal_network = models.ManyToManyField('Member', through='Relationship')
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def is_favorite(self, other_member): 
        """
        :param other_member:
        :return: True if the email is in the favorite list of the member
        """
        for relation in self.relation.all():
            if relation == other_member: 
                return True
        return False
    
    class Meta:
        app_label = 'C4CApplication'
