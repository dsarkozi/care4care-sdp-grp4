from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.views.utils import create_user
from C4CApplication.models.job import Job
from C4CApplication.models.member import Member
from django.core.exceptions import PermissionDenied


class ParticipateJobRedirectView(RedirectView):
    
    url = ""
    
    user = None

    def dispatch(self, request, *args, **kwargs):
        # Create the object representing the user
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])

        return super(ParticipateJobRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        
        mail_member_choiced = kwargs['mail']
        job_id = kwargs['pk']
        self.url = "/jobdetails/"+str(job_id)
        
        #Recuperation du job
        job = Job.objects.filter(id=job_id)
        if len(job)!=1 :
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        job = job[0]
        
        #Test du user
        if self.user==None:
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        if self.user.db_member==None:
            return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)
        
        #Actions buttons
        if mail_member_choiced == self.user.db_member.mail :    #Clicked on delete job
            self.user.delete_job(job.id)
            self.url = "/"
        elif mail_member_choiced == 'no_response@care4care.com' :   #Clicked on participate/stop participating    
            if self.user.db_member in job.member_set.all() :
                self.user.stop_participate_job(job.number, job.mail)
            elif not job.accepted :
                self.user.accept_job(job.number, job.mail)
        elif mail_member_choiced == 'no_response_regular@care4care.com':
            self.url = "/jobdetails/"+str(job.regular_job.id)
            if self.user.db_member in job.member_set.all() :
                self.user.stop_participate_job(job.number, job.mail)
            elif not job.accepted :
                self.user.accept_job(job.number, job.mail)
        else :  #Clicked on Choice this member
            self.user.choose_participant_for_job(job.number, job.mail, mail_member_choiced)
            
        
        return super(ParticipateJobRedirectView, self).get(request, *args, **kwargs)