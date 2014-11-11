from C4CApplication.models import Branch


class BranchGuard():
    
    def create_branch(self, member, fields): 
        """ returns True if creation is done """
        # TODO 
        return True
    
    def get_branch(self, member, criteria): 
        """ returns a QuerySet """
        # TODO 
        return None
    
    def modify_name(self, member, identity, modification): #TODO keep this function ? Because changing private key is difficult in db
        # TODO
        return True
    
    def modify_town(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_branch_officer(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_adress(self, member, identity, modification): 
        # TODO
        return True
    
    def add_job(self, member, identity, job): 
        # TODO
        return True
    
    def remove_job(self, member, identity, job): 
        # TODO
        return True