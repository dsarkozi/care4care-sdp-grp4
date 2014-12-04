from time import strftime, gmtime
import os
from django.core.files import File


from django.db import models
from localflavor.be.forms import BEPostalCodeField

from django.core.files.storage import FileSystemStorage
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        if self.exists(name):
            self.delete(name)
        return name


class Member(models.Model):
    mail = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    picture = models.ImageField(null=True, blank=True, upload_to="images/images_profile/", storage=OverwriteStorage())
    birthday = models.DateField(blank=True, null=True)   #'yyyy-mm-dd'   #TODO default ? Really ?
    
    TAG_REVERSE = {
        1         : 'non_member',               #000001
        2         : 'member',                   #000010
        4         : 'verified',                 #000100
        8         : 'volunteer',                #001000
        16        : 'branch_officer',           #010000
        32        : 'bp_admin',                 #100000
    }
    
    TAG_CHOICE = (
        (1, 'Non member'),
        (2, 'Member'),
        (4, 'Verified'),
        (8, 'Volunteer'),
        (16, 'Branch officer'),
        (32, 'BP admin'),
    )
    
    TAG = {
        'non_member'             : 1,   #000001
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
