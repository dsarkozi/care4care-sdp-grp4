from C4CApplication.models import Job, NonMember

class JobView():
    """
    This class represents the view for the Jobs
    """
    
    # TODO
    def is_job_visible(self, job, db_member):
        member = None # get_member TODO
        # unserailize member
        
        member.is_job_visible(job, db_member)
        
        # redirect to useless page
        # inject next data 
        # reload the page 
    
    # TODO
    def see_job_details(self, job_number, job_creator_mail):
        member = None # get_member TODO
        # unserailize member
        
        member.see_job_details(job_number, job_creator_mail)
        
        # redirect to useless page
        # inject next data 
        # reload the page 
      
    # TODO  
    def get_visible_job_list(self, show_offers):
        member = None # get_member TODO
        # unserailize member
        
        member.get_visible_job_list(show_offers)
        
        # redirect to useless page
        # inject next data 
        # reload the page        
    
    # TODO
    def get_involved_job_list(self, show_offers):
        member = None # get_member TODO
        # unserailize member
        
        member.get_involved_job_list(show_offers)
        
        # redirect to useless page
        # inject next data 
        # reload the page
       
    # TODO 
    def accept_job(self, job_number, job_creator_mail):
        member = None # get_member TODO
        # unserailize member
        
        member.accept_job(job_number, job_creator_mail)
        
        # redirect to useless page
        # inject next data 
        # reload the page  
    
    # TODO
    def create_job(self, start_time, time, branch_name, comment=None, frequency=0, km=0,
                   category=1, address=None, visibility='anyone'):     
        member = None # get_member TODO
        # unserailize member
        
        member.create_job(start_time, time, branch_name, comment=None, frequency=0, km=0, category=1, address=None, visibility='anyone')
        
        # redirect to useless page
        # inject next data 
        # reload the page 
    
    # TODO
    def register_job_done(self, job_id, helped_one_email):
        member = None # get_member TODO
        # unserailize member
        
        member.register_job_done(job_id, helped_one_email)
        
        # redirect to useless page
        # inject next data 
        # reload the page 