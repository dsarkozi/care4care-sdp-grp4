from django.views.generic import DetailView
from C4CApplication.models.member import Member
from C4CApplication.models.job import Job
from C4CApplication.views.utils import create_user
from django.core.exceptions import PermissionDenied


class AcceptBillView(DetailView): 
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/AcceptBill.html"
    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])

        return super(AcceptBillView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(AcceptBillView, self).get_context_data()
        context['member'] = self.user.db_member
        return context
