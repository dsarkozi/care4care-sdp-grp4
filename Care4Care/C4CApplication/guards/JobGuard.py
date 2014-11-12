from C4CApplication.models import Job


class JobGuard():
    
    def create_job(self, member, fields): 
        """ returns True if creation is done """
        job = Branch() #TODO primary key...
        job.mail = fields["mail"]
        if fields["done"] != None :
            job.done = fields["done"]
        if fields["comment"] != None :
            job.comment = fields["comment"]
        job.start_time = fields["start_time"]
        job.frequency = fields["frequency"]
        if fields["km"] != None :
            job.km = fields["km"]
        job.time = fields["time"]
        job.category = fields["job_category"]
        job.type = fields["type"]
        if fields["address"] != None :
            job.address = fields["address"]
        job.branch = fields["branch"]
        job.save()
        return True
    
    def get_jobs(self, criteria): 
        """ returns a QuerySet """
        jobs = Job.objects.all(); 
        for field, value in criteria : 
            jobs = jobs.filter(field=value)
        return jobs
    
    def modify_done(self, member, identity, modification): 
        job = Job.objects.get()#TODO primary key = identity
        if not ((job.type and member.mail==job.member_set[0]) or (not job.type and member.mail==job.member_set[1])) : #if it is not the helped one
            return False
        job.done = modification
        job.save()
        return True
    
    def modify_comment(self, member, identity, modification):  
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.member_set[0] and member.mail!=job.member_set[1] : #if it is not the helped one neither the helper
            return False
        job.comment = modification
        job.save()
        return True
    
    def modify_start_time(self, member, identity, modification): 
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.mail : #if it is not the creator
            return False
        job.start_time = modification
        job.save()
        return True
    
    def modify_frequency(self, member, identity, modification): 
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.mail : #if it is not the creator
            return False
        job.frequency = modification
        job.save()
        return True
    
    def modify_km(self, member, identity, modification): 
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.mail : #if it is not the creator
            return False
        job.km = modification
        job.save()
        return True
    
    def modify_time(self, member, identity, modification):
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.mail : #if it is not the creator
            return False
        job.time = modification
        job.save()
        return True
    
    def modify_category(self, member, identity, modification):
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.mail : #if it is not the creator
            return False
        job.category = modification
        job.save()
        return True
    
    def modify_type(self, member, identity, modification): 
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.mail : #if it is not the creator
            return False
        job.type = modification
        job.save()
        return True
    
    def modify_address(self, member, identity, modification): 
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.mail : #if it is not the creator
            return False
        job.address = modification
        job.save()
        return True
    
    def modify_accepted(self, member, identity, modification):
        job = Job.objects.get()#TODO primary key = identity
        if member.mail!=job.member_set[0] and member.mail!=job.member_set[1] : #if it is not the helped one neither the helper
            return False
        job.accepted = modification
        job.save()
        return True