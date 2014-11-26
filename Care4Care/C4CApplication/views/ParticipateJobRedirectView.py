from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.views.utils import create_user
from C4CApplication.models.job import Job
from C4CApplication.models.member import Member


class ParticipateJobRedirectView(RedirectView):
    
    url = ""
    
    connected_member = None

    def dispatch(self, request, *args, **kwargs):
        # Create the object representing the user
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.connected_member = create_user(self.request.session['email'])

        return super(ParticipateJobRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        job_id = kwargs['pk']
        self.url = "/jobdetails/"+str(job_id)
        
        #Recuperation du job
        job = Job.objects.filter(id=job_id)
        if len(job)!=1 :
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        job = job[0]
        
        #Test du connected_member
        if self.connected_member==None:
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        if self.connected_member.db_member==None:
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        
        #Action du bouton
        if self.connected_member.db_member in job.member_set.all() :
            self.connected_member.stop_participate_job(job.number, job.mail)
        elif not job.accepted :
            self.connected_member.accept_job(job.number, job.mail)
        
        return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)