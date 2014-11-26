from django.views.generic import FormView
from C4CApplication.models.job import Job
from C4CApplication import models
from C4CApplication.meta import Member, User
from C4CApplication.views.JobDetailsView import JobDetailsView
from C4CApplication.views.forms.ConfirmJobDoneForm import ConfirmJobDoneForm
from C4CApplication.views.utils import create_user

from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy

class ConfirmJobDoneView(FormView, JobDetailsView):
    
    template_name = "C4CApplication/ConfirmJobDoneView.html"
    form_class = ConfirmJobDoneForm
    success_url = reverse_lazy("myc4c")
    user = None

    def get_object(self):
        
        job = super(ConfirmJobDoneView, self).get_object()
    
        return job
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])

        return super(ConfirmJobDoneView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ConfirmJobDoneView, self).get_context_data(**kwargs)
        
        # Creates the form and change the context
        confirm_job_done_form = ConfirmJobDoneForm(auto_id=False)

        context['confirm_job_done_form'] = confirm_job_done_form
        return context

    
    def form_valid(self, form):
        # TODO test if the member has session variables !! -> redirection
        if ConfirmJobDoneView.user is None:
            ConfirmJobDoneView.user = models.Member.objects.get(mail=self.request.session['email'])

        # value entered in the integer field
        time_to_pay = form.cleaned_data['time_to_pay']
        
        job = self.get_object()
        # retrieve helped_one, None if impossible to retrieve
        helped_one_mail = None
        if job.type : 
            helped_one_mail = job.mail 
        elif len(job.member_set.all()) <= 2 : 
            for member in job.member_set.all() : 
                if member.mail != job.mail : helped_one_mail = member.mail

        # register that the job is done
        self.user.register_job_done(job.number, job.mail, helped_one_mail, time_to_pay)
        
        return super(ConfirmJobDoneView, self).form_valid(form)