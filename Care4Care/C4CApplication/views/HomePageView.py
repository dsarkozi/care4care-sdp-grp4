from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "C4CApplication/HomePage.html"
    
    def demand_job_list(self):
        member = None # get_member TODO
        return member.get_visible_jobs_list(True)
        
    def offert_job_list(self):
        member = None # get_member TODO
        return member.get_visible_jobs_list(False)
    
    def click_on_job(self, job_number, job_creator_mail):
        member = None # get_member TODO
        # unserailize member
        
        job = member.see_job_details(job_number, job_creator_mail)
        
        # redirect to job page