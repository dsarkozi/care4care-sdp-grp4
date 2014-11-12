from C4CApplication.models import Message


class MessageGuard():
    
    def create_message(self, member, fields): 
        """ returns True if creation is done """
        message = Message.create() #TODO add primary key
        message.mail = fields["mail"]
        message.subject = fields["subject"]
        if fields["type"] != None :
            message.type = fields["type"]
        if fields["status"] != None :
            message.type = fields["status"]
        message.date = fields["date"]
        message.save()
        return True
    
    def get_messages(self, member, criteria): 
        """ returns a QuerySet """
        message = Message.objects.all(); #TODO add condition : user can access this message
        for field, value in criteria : 
            message = message.filter(field=value)
        return message
    
    def modify_status(self, member, identity, modification): 
        #need primary key to get the message
        #TODO implementation of message in db not yet fixed
        return True