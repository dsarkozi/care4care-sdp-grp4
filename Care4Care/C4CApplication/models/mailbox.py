from django.db import models


class Mailbox(models.Model):
    ''' Il ne s'agit pas d'une boite mail, mais simplement d'un lien entre un Member et un Message.
    Cela permet d'avoir un status pour le message par personne. '''
    member_receiver = models.ForeignKey('Member')    #Person who receives the mail
    message = models.ForeignKey('Message')
    status = models.BooleanField(default=False) #False = notRead, True = read