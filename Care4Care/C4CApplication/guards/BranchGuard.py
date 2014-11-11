from C4CApplication.models import Branch
from django.db.models.query import QuerySet

class BranchGuard():
    
    def create_branch(self, member, fields):
        """ returns True if the creation is done """
        if(member.tag!=5): # if not bp-admin
            return False
        branch = Branch( name = fields["name"] )
        branch.town = fields["town"]
        branch.branch_officer = fields["branch_officer"]
        branch.adress = fields["adress"]
        
        branch.save()
        return True
    
    def get_branch(self, criteria): 
        """ returns a QuerySet """
        result = Branch.objects.all(); 
        for field, value in criteria : 
            result = result.filter(field=value)
        return result
    
    def modify_name(self, member, identity, modification): #TODO keep this function ? Because changing private key is difficult in db
        if(member.tag<4):
            return False
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