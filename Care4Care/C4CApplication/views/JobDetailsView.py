from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from C4CApplication.models.job import Job
from django.views.generic import FormView

class JobDetailsView(DetailView, FormView):
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/JobDetails.html"
    connected_member = None
    #TODO form class
    
    def dispatch(self, request, *args, **kwargs):
        # Create the object representing the user
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.connected_member = create_user(self.request.session['email'])

        return super(JobDetailsView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = {}
        context = super(JobDetailsView, self).get_context_data(**context)
        context['form'] = self.form
        context['member'] = self.connected_member.db_member
        return context

    def form_valid(self, form):

        #TODO tratement de la date

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
    
        return job