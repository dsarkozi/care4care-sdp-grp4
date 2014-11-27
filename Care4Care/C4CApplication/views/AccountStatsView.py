from django.core.exceptions import PermissionDenied
from django.views.generic.list import ListView
from C4CApplication.models.job import Job

from C4CApplication.views.utils import create_user


class AccountStatsView(ListView):
    template_name = "C4CApplication/accountAndStats.html"
    context_object_name = "job_list"
    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])
        self.queryset = Job.objects.filter(mail=self.request.session['email'])     #TODO Change this with db_member.job
        return super(AccountStatsView, self).dispatch(request, *args, **kwargs)

