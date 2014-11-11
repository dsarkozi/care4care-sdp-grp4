from C4CApplication.models import Branch
from django.db.models.query import QuerySet

class BranchGuard():
    
    def create_branch(self, member, fields):
        """ returns True if the creation is done """
        if(member.tag<5): # if not bp-admin
            return False
        branch = Branch( name = fields["name"] )
        branch.town = fields["town"]
        branch.branch_officer = fields["branch_officer"]
        branch.address = fields["address"]
        branch.save()
        return True
    
    def get_branches(self, criteria): 
        """ returns a QuerySet """
        branches = Branch.objects.all(); 
        for field, value in criteria : 
            branches = branches.filter(field=value)
        return branches
    
    def modify_name(self, member, identity, modification): #TODO keep this function ? Because changing private key is difficult in db
        branch = Branch.objects.get(identity)
        if(member.tag<5 & member.mail != branch.branch_officer): # if not bp-admin neither the Branch-officer 
            return False
        branch.name = modification
        branch.save()
        return True
    
    def modify_town(self, member, identity, modification): 
        branch = Branch.objects.get(identity)
        if(member.tag<5 & member.mail != branch.branch_officer): # if not bp-admin neither the Branch-officer 
            return False
        branch.town = modification
        branch.save()
        return True
    
    def modify_branch_officer(self, member, identity, modification): 
        if(member.tag<5):
            return False
        result = Branch.objects.get(identity)
        result.branch_officer = modification
        result.save()
        return True
    
    def modify_address(self, member, identity, modification): 
        branch = Branch.objects.get(identity)
        if(member.tag<5 & member.mail != branch.branch_officer): # if not bp-admin neither the Branch-officer 
            return False
        branch.address = modification
        branch.save()
        return True
    
    #TODO job is an Entry.objects.get() ? if not, need to create it before adding it
    def add_job(self, member, identity, job):
        if(job.mail != member.mail) : #TODO necessary ?
            return False
        branch = Branch.objects.get(identity)
        allowed = False
        for br in member.branch :
            if (branch == br) :
                allowed = True
        if (~allowed) :
            return False
        branch.job_set.add(job)
        return True
    
    def remove_job(self, member, identity, job): 
        if(job.mail != member.mail) : #TODO necessary ? And who can delete a job?
            return False
        branch = Branch.objects.get(identity)
        allowed = False
        for br in member.branch :
            if (branch == br) :
                allowed = True
        if (~allowed) :
            return False
        #need to Entry.object.get(job) before removing it, but not primary_key...
        branch.job_set.remove(job)
        return True