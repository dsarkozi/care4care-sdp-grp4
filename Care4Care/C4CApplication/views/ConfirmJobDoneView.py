from django.views.generic import FormView
from C4CApplication.models.job import Job

class ConfirmJobDoneView(FormView, JobDetailsView):
    
    template_name = "C4CApplication/ConfirmJobDoneView.html"
    form_class = ConfirmJobDoneForm
    success_url = "myc4c"
    member = None

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
    
        return job
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        return super(ConfirmJobDoneView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ConfirmJobDoneView, self).get_context_data(**kwargs)
        
        # Creates the form and change the context
        conf_job_done_form = ConfirmJobDoneForm(auto_id=False)

        context['conf_job_done_form'] = conf_job_done_form
        return context

    
    def form_valid(self, form):
        # TODO test if the member has session variables !! -> redirection
        if ConfirmJobDoneView.member is None:
            ConfirmJobDoneView.member = Member.objects.get(mail=self.request.session['email'])

        # value entered in the integer field
        time_to_pay = form.cleaned_data['time_to_pay']
        
        # retrieve helped_one, None if impossible to retrieve
        helped_one = None
        if len(job.member_set.all()) <= 2 : 
            for member in job.member_set.all() : 
                if member.mail != job.mail : helped_one = member
                
        # register that the job is done
        ConfirmJobDoneView.member.register_job_done(self, job.id, job.mail, helped_one.mail, time_to_pay) # comment je connais le job ?

        return super(ConfirmJobDoneView, self).form_valid(form)