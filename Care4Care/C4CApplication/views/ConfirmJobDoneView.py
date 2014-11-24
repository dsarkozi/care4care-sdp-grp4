from django.views.generic import FormView
from C4CApplication.models.job import Job

class ConfirmJobDoneView(FormView):
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/ConfirmJobDoneView.html"
    member = None

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
    
        return job
    
    def form_valid(self, form):
        # TODO test if the member has session variables !! -> redirection
        if ConfirmJobDoneView.member is None:
            ConfirmJobDoneView.member = Member.objects.get(mail=self.request.session['email'])

        # recupere la valeur d'input
        # verifier que cette valeur est ok
        ConfirmJobDoneView.member.register_job_done(job_id, helped_one_email) # comment je connais le job ?

        return super(ConfirmJobDoneView, self).form_valid(form)