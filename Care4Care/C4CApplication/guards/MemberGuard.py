from C4CApplication.models import Member
from django.db.models.query import QuerySet


class MemberGuard():
    
    def create_member(self, fields): 
        """ returns True if the creation is done """
        member = Member( mail = fields["mail"] )
        
        member.first_name = fields["first_name"]
        member.last_name = fields["last_name"]
        #member.picture = fields["picture"]
        member.birthday = fields["birthday"]
        if fields["tag"] < 0 or fields["tag"] > 6 : return False
        member.tag = fields["tag"]
        member.status = fields["status"]
        member.mobile = fields["mobile"]
        member.telephone = fields["telephone"]
        member.register_date = fields["register_date"]
        member.dash_board_text = fields["dash_board_text"]
        member.address = fields["address"]
        if fields["visibility"] < 0 and fields["visibility"] > 3 : return False
        member.visibility = fields["visibility"]
        member.time_credit = fields["time_credit"]
        
        member.save()
        return True
    
    def get_members(self, member, criteria): 
        """ returns a QuerySet of all the objects in the database 
        filtered by the criteria dictionary of the form (field, value) """
        result = Member.objects.all(); 
        for field, value in criteria : 
            result = result.filter(field=value)
            
        # TODO check visibility of the searched people
        #result.exlude(visibility=) ?
        return result
    
    def modify_mail(self, member, identity, modification): 
        """ returns True if the value of the field mail as been replaced by the value of modification
        for the member identified by identity """
        if member.type != 5 : # not a bp admin
            return False
        
        to_change = Member.objects.get(mail=identity) # Not sure about this 
        to_change.mail = modification
        to_change.save()
        return True
    
    def modify_first_name(self, member, identity, modification): 
        """ returns True if the value of the field first_name as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.first_name = modification
        to_change.save()
        return True
    
    def modify_last_name(self, member, identity, modification): 
        """ returns True if the value of the field last_name as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.last_name = modification
        to_change.save()
        return True
    
    def modify_picture(self, member, identity, modification): 
        """ returns True if the value of the field picture as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.picture = modification
        to_change.save()
        return True
    
    def modify_birthday(self, member, identity, modification): 
        """ returns True if the value of the field birthday as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.birthday = modification
        to_change.save()
        return True
    
    # Done by the system. Useful to give a member in param ????
    def modify_tag(self, member, identity, modification): 
        """ returns True if the value of the field tag as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.type < 4 : # not a bp admin
            return False
        if member.type == 4 :
            no_valid_branch_officer = True
            for b in to_change.branch : 
                if b.branch_officer == member.mail : no_valid_branch_officer = False
            if no_valid_branch_officer : return False
        
        to_change = Member.objects.get(mail=identity)
        to_change.tag = modification
        to_change.save()
        return True
    
    def modify_status(self, member, identity, modification): 
        """ returns True if the value of the field status as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.status = modification
        to_change.save()
        return True
    
    def modify_mobile(self, member, identity, modification): 
        """ returns True if the value of the field mobile as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.mobile = modification
        to_change.save()
        return True
    
    def modify_telephone(self, member, identity, modification): 
        """ returns True if the value of the field telephone as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.telephone = modification
        to_change.save()
        return True
    
    def modify_dash_board_text(self, member, identity, modification): 
        """ returns True if the value of the field dash_board_text as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)        
        to_change.dash_board_text = modification
        to_change.save()
        return True
    
    def modify_address(self, member, identity, modification): 
        """ returns True if the value of the field address as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.address = modification
        to_change.save()
        return True
    
    def add_visibility(self, member, identity, option): 
        """ returns True if the value of option is has been added to the field visibility """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.visibility = to_change.visibility + option
        to_change.save()
        return True
    
    def remove_visibility(self, member, identity, option): 
        """ returns True if the value of option is has been removed from the field visibility """
        to_change = Member.objects.get(mail=identity)
        if member.mail != to_change.mail : 
            return False
        
        to_change.visibility = to_change.visibility - option
        to_change.save()
        return True
    
    def modify_time_credit(self, member, identity, modification): 
        """ returns True if the value of the field time_credit as been replaced by the value of modification
        for the member identified by identity """
        to_change = Member.objects.get(mail=identity)        
        if member.mail != to_change.mail : 
            return False
        
        to_change.time_credit = modification
        to_change.save()
        return True
    
    def add_branch(self, member, identity, branch): 
        """ returns True if the branch is added in the list of branches of the member identified by identity 
        Member member : the member that wants to add the branch for identity
        Branch branch : the branch that the Member identity joins """
        to_change = Member.objects.get(mail=identity)        
        if member.mail != to_change.mail : 
            return False
        
        to_change.branch.add(branch) 
        return True
    
    def remove_branch(self, member, identity, branch): 
        """ returns True if the branch is removed from the list of branches of the member identified by identity """
        to_change = Member.objects.get(mail=identity)        
        if member.mail != to_change.mail and member.type < 4 : # si membre lui-meme ou bp admin ou branch off, ok, sinon False
            return False
        if member.type == 4 and member.branch != branch : # si branch officer mais d'un autre branche
            return False
        
        to_change.branch.remove(branch) 
        return True
    
    def add_favorite(self, member, identity, favorite): 
        """ returns True if the favorite is added in the list of favorites of the member identified by identity """
        to_change = Member.objects.get(mail=identity)        
        if member.mail != to_change.mail : 
            return False
        
        to_change.favorite.add(favorite) 
        return True
    
    def remove_favorite(self, member, identity, favorite): 
        """ returns True if the favorite is removed from the list of favorites of the member identified by identity """
        to_change = Member.objects.get(mail=identity)        
        if member.mail != to_change.mail : 
            return False
        
        to_change.favorite.remove(favorite) 
        return True
    
    # Optional
    """def add_ignored(self, member, identity, ignored): """ 
    """ returns True if the ignored person is added in the list of ignored of the member identified by identity """
    """to_change = Member.objects.get(mail=identity)        
        if member.mail != to_change.mail : 
            return False
        
        to_change.ignored.add(ignored) 
        return True
    
    def remove_ignored(self, member, identity, ignored): 
        # TODO
        return True"""
    
    def add_job(self, member, identity, job): 
        """ returns True if the job is added in the list of jobs of the member identified by identity """
        to_change = Member.objects.get(mail=identity)        
        if member.mail != to_change.mail : 
            return False
        
        to_change.job.add(job) 
        return True
    
    def remove_job(self, member, identity, job): 
        """ returns True if the favorite is removed from the list of favorites of the member identified by identity """
        to_change = Member.objects.get(mail=identity)        
        if member.mail != to_change.mail : 
            return False
        
        to_change.job.remove(job) 
        return True
