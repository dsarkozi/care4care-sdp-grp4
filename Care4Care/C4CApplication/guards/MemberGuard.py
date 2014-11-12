from C4CApplication.models import Member
from django.db.models.query import QuerySet


class MemberGuard():
    
    def create_member(self, fields): 
        """ returns True if the creation is done """
        member = Member( mail = fields["mail"] )
        
        member.first_name = fields["first_name"]
        member.last_name = fields["last_name"]
        member.picture = fields["picture"]
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
    
    def modify_accepted(self, member, identity, modification): 
        # TODO
        return True
    
    def add_branch(self, member, identity, branch): 
        # TODO
        return True
    
    def remove_branch(self, member, identity, branch): 
        # TODO
        return True
    
    def add_favorite(self, member, identity, favorite): 
        # TODO
        return True
    
    def remove_favorite(self, member, identity, favorite): 
        # TODO
        return True
    
    def add_ignored(self, member, identity, ignored): 
        # TODO
        return True
    
    def remove_ignored(self, member, identity, ignored): 
        # TODO
        return True
    
    def add_job(self, member, identity, job): 
        # TODO
        return True
    
    def remove_job(self, member, identity, job): 
        # TODO
        return True
    
    def add_message_sent(self, member, identity, message_sent): 
        # TODO
        return True
    
    def remove_message_sent(self, member, identity, message_sent): 
        # TODO
        return True
    
    def add_message_received(self, member, identity, message_received): 
        # TODO
        return True
    
    def remove_message_received(self, member, identity, message_received): 
        # TODO
        return True
