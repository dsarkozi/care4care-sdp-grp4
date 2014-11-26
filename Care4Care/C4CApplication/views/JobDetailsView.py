from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from C4CApplication.models.job import Job


class JobDetailsView(DetailView):
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/JobDetails.html"
    connected_member = None
    
    def dispatch(self, request, *args, **kwargs):
        #if 'email' not in self.request.session:
        #    raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        #self.connected_member = create_user(self.request.session['email'])
        self.connected_member = create_user("kim.mens@gmail.com")

        return super(JobDetailsView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = {}
        context = super(JobDetailsView, self).get_context_data(**context)
        context['connected_member'] = self.connected_member.db_member
        return context

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
    
        return job