from django.views.generic import DetailView
from C4CApplication.models.member import Member
from C4CApplication.models.job import Job
from django.core.exceptions import PermissionDenied


class AcceptBillView(DetailView): 
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/AcceptBill.html"
    
    def get_object(self):
        
        job = super(AcceptBillView, self).get_object()
    
        return job
    
    def get_context_data(self, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        context = super(AcceptBillView, self).get_context_data(**kwargs)
        member = Member.objects.get(mail=self.request.session['email'])
        context['member'] = member
        return context
    
    
    
    