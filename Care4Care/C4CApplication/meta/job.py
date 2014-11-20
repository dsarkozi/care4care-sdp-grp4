from C4CApplication.models import Job, NonMember

class JobView():
    """
    This class represents the view for the Jobs
    """
    
    # TODO
    def register_job_done(self, job_id, helped_one_email):
        member = None # get_member TODO
        # unserailize member
        
        member.register_job_done(job_id, helped_one_email)
        
        # redirect to useless page
        
        # inject next data 
        
        # reload the page 