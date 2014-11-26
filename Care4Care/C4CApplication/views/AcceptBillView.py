from django.views.generic import DetailView
#from C4CApplication.models.member import Member
from C4CApplication.models.job import Job


class AcceptBillView(DetailView): 
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/AcceptBill.html"
    
    def get_object(self):
        
        job = super(AcceptBillView, self).get_object()
    
        return job
    
    
    
    
    
    
    
    
    
    