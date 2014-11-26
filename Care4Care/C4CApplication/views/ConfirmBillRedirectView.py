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
            res = member.accept_bill(job.number, job.mail, job.time)
        else : # pressed contest
            print("send mail to bp admin !")
            
        return super(ConfirmBillRedirectView, self).get(request, *args, **kwargs)