from C4CApplication.models import Message


class MessageGuard():
    
    def create_job(self, member, fields): 
        """ returns True if creation is done """
        # TODO 
        return True
    
    def get_job(self, member, criteria): 
        """ returns a QuerySet """
        # TODO 
        return None
    
    def modify_subject(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_type(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_status(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_date(self, member, identity, modification): 
        # TODO
        return True