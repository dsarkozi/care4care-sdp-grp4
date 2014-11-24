from django.views.generic import FormView
from C4CApplication.models.job import Job

class ConfirmJobDoneView(FormView):
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/confirmjobdoneview.html"

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
    
        return job
    