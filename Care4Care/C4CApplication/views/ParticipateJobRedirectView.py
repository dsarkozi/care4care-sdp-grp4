from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.views.utils import create_user
from C4CApplication.models.job import Job
from C4CApplication.models.member import Member


class ParticipateJobRedirectView(RedirectView):
    
    url = ""

    @never_cache
    def get(self, request, *args, **kwargs):
        #user = create_user(self.request.session['email'])
        job_id = kwargs['pk']
        self.url = "/jobdetails/"+str(job_id)
        
        job = Job.objects.filter(id=job_id)
        if len(job)!=1 :
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        job = job[0]
        
        connected_member = create_user("kim.mens@gmail.com")
        if connected_member==None:
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        if connected_member.db_member==None:
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        
        if connected_member.db_member in job.member_set.all() :
            connected_member.stop_participate_job(job.number, job.mail)
        elif not job.accepted :
            connected_member.accept_job(job.number, job.mail)
        
        return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)