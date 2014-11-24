from django.views.generic import DetailView
from C4CApplication.models.job import Job

class JobDetailsView(DetailView):
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/JobDetails.html"

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
    
        return job