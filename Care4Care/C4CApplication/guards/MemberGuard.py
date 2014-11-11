from C4CApplication.models import Member


class MemberGuard():
    
    def create_member(self, member, fields): 
        """ returns True if creation is done """
        # if member as not the authorization return False 
        # else 
        mail = fields["mail"]
        first_name = fields["first_name"]
        last_name = fields["last_name"]
        picture = fields["picture"]
        birthday = fields["birthday"]
        if fields["tag"] >= 0 and fields["tag"] <= 6 : 
            tag = fields["tag"]
        status = fields["status"]
        mobile = fields["mobile"]
        telephone = fields["telephone"]
        register_date = fields["register_date"]
        dash_board_text = fields["dash_board_text"]
        adresse = fields["adresse"]
        if fields["visibility"] >= 0 and fields["visibility"] <= 3 :
            visibility = fields["visibility"]
        time_credit = fields["time_credit"]
        return True
    
    def get_members(self, member, criteria): 
        """ returns a QuerySet """
        # TODO 
        return None
    
    def modify_mail(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_first_name(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_last_name(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_picture(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_birthday(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_tag(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_status(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_mobile(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_telephone(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_registered_date(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_dash_board_text(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_adresse(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_visibility(self, member, identity, modification): 
        # TODO
        return True
    
    def modify_time_credit(self, member, identity, modification): 
        # TODO
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
