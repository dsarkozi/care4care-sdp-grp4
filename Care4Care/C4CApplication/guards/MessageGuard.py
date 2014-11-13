from C4CApplication.models import Message


class MessageGuard():
    
    def create_message(self, fields): 
        """ returns True if creation is done """
        message = Message.create() #TODO add primary key
        message.mail = fields["mail"]
        message.subject = fields["subject"]
        if fields["type"] != None :
            message.type = fields["type"]
        message.date = fields["date"]
        message.content = fields["content"]
        message.save()
        return True
    
    def send_message(self, fields):
        mailbox = Mailbox.create()
        if fields["status"] != None :
            mailbox.status = fields["status"]
        mailbox.member = fields["member"]
        mailbox.message = fields["message"]
    
    def get_received_messages(self, member): 
        """ returns a list """
        mailboxes = Mailbox.objects.all()
        mailboxes = mailboxes.filter(member=member.mail)
        messages = []
        for mailbox in mailboxes :
            messages.append(Message.objects.get(id=mailbox.message))
        return messages
    
    def get_sent_messages(self, member): 
        """ returns a QuerySet """
        messages = Message.objects.all()
        messages = messages.filter(mail = member.mail)
        return messages
    
    def get_status(self, member, message):
        """ returns a boolean """
    
    def modify_status(self, member, identity, modification): 
        if member!=identity["member"] :
            return False
        mailBox = Mailbox.objects.get(member = identity["member"], message=identity["message"])
        mailBox.status = modification
        return True