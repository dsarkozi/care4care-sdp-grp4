from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.models.member import Member
from C4CApplication.models.job import Job
from C4CApplication.views.utils import create_user
from C4CApplication.meta.user import User
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied


class ConfirmBillRedirectView(RedirectView):

    url = reverse_lazy("myc4c")
    user= None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(ConfirmBillRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        job_id = kwargs['pk']
        confirmation = int(kwargs['confirm'])
        
        # get the job 
        job = Job.objects.get(id=job_id)
        
        # get member 
        member = create_user(self.request.session['email'])
        
        if confirmation == 1 : # pressed confirm
            member.accept_bill(job.number, job.mail, job.time)
        else : # pressed contest
            helper_mail = None
            if not job.type:  # offer
                helper_mail = job_creator_mail
            else:  # demand
                helper_mail = None
                participants = job.member_set.all()
                for participant in participants:
                    if participant.mail != member.db_member.mail:
                        helper_mail = participant.mail
                        break

            if helper_mail is not None : 
                res = member.refuse_bill(job.number, job.mail, helper_mail)
                print("Refused : "+str(res))
            
        return super(ConfirmBillRedirectView, self).get(request, *args, **kwargs)