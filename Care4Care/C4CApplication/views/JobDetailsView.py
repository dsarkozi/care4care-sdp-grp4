from django.views.generic import DetailView
from django.views.generic import FormView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.contrib.comments import get_form
from C4CApplication.views.utils import create_user
from C4CApplication.models.job import Job
from C4CApplication.views.forms.JobRegularForm import JobRegularForm


class JobDetailsView(DetailView, FormView):
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/JobDetails.html"
    member = None
    form_class = JobRegularForm
    job = None
    
    def dispatch(self, request, *args, **kwargs):
        # Create the object representing the user
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.member = create_user(self.request.session['email'])

        return super(JobDetailsView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = {}
        context = super(JobDetailsView, self).get_context_data(**context)
        context['form'] = JobRegularForm(job=self.job, auto_id=False)
        context['member'] = self.member.db_member
        context['connected'] = 'email' in self.request.session
        return context

    def form_valid(self, form):
        #TODO tratement de la date
        pass

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
        self.job = job
    
        return job