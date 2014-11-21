from django.db import models


class Relationship(models.Model):
    member_source = models.ForeignKey('Member', related_name = 'source')
    member_target = models.ForeignKey('Member', related_name = 'target')
    
    '''
    TYPE = {
        'favorite'            : 1,   #000001
        'ignored'             : 2,   #000010
        'personal_network'    : 4,   #000100
    }
    #type_of_relation = models.SmallIntegerField(default=1)
    '''