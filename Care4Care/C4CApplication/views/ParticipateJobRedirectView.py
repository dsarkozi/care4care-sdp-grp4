from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.models.job import Job
from C4CApplication.models.member import Member


class ParticipateJobRedirectView(RedirectView):

    job = None
    
    url = ""

    @never_cache
    def get(self, request, *args, **kwargs):
        #member = Member.objects.filter(mail=request.session['email'])
        job_id = kwargs['pk']
        self.job = Job.objects.filter(id=job_id)
        self.url = "/jobdetails/"+str(job_id)
        #member.accept_job(job.number, job.mail)
        return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)