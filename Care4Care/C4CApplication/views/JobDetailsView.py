from django.views.generic import DetailView
from django.views.generic import FormView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.contrib.comments import get_form
from C4CApplication.views.utils import create_user
from C4CApplication.models.job import Job
from C4CApplication.views.forms.JobRegularForm import JobRegularForm
from gc import get_objects


class JobDetailsView(DetailView, FormView):
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/JobDetails.html"
    success_url = "/jobdetails/"
    member = None
    form_class = JobRegularForm
    job = None
    
    def dispatch(self, request, *args, **kwargs):
        # Create the object representing the user
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.member = create_user(self.request.session['email'])
        self.job = self.get_object()

        return super(JobDetailsView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = {}
        context = super(JobDetailsView, self).get_context_data(**context)
        if self.job.frequency == 2 :
            context['form'] = JobRegularForm(job=self.job, nbr_prop=2, auto_id=False)
        else :
            context['form'] = JobRegularForm(job=self.job, auto_id=False)
        context['member'] = self.member.db_member
        context['connected'] = 'email' in self.request.session
        return context

    def form_valid(self, form):
        '''
        Here, the self.job is so the regular job.
        '''
        self.success_url += str(self.job.id)
        
        date = form.cleaned_data['proposition']
        creator_of_regular_job = create_user(self.job.mail)
        new_job = creator_of_regular_job.create_job(self.job.branch.name, self.job.title, date, self.job.type, '', '',\
                                          self.job.start_time, 0, self.job.km, self.job.duration, self.job.category,\
                                          self.job.other_category, self.job.place, 'anyone', '')
        if new_job :
            new_job.visibility = self.job.visibility
            self.job.job_set.add(new_job)
            new_job.member_set.add(self.member.db_member)
        
        return super(JobDetailsView, self).form_valid(form)

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
    
        return job