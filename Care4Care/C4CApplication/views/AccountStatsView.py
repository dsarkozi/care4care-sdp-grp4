from django.core.exceptions import PermissionDenied
from django.db.models.aggregates import Avg, Sum
from django.views.generic.base import TemplateView
import time

from C4CApplication.models.job import Job
from C4CApplication.tests.utils import printy_set, printy
from C4CApplication.views.utils import create_user


class AccountStatsView(TemplateView):
    template_name = "C4CApplication/accountAndStats.html"
    user = None
    jobset = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])
        self.jobset = Job.objects.filter(mail=self.request.session['email'])     #TODO Change this with db_member.job
        return super(AccountStatsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AccountStatsView, self).get_context_data(**kwargs)
        context['jobAmount'] = self.jobset.count()
        context['jobAverageTime'] = time.strftime('%H:%M:%S', time.gmtime(self.jobset.aggregate(Avg('time'))['time__avg']))
        context['jobTotalDistance'] = self.jobset.aggregate(Sum('km'))['km__sum']
        categoryStats = dict()
        for job in self.jobset:
            cat = job.CAT_DICT[job.category]
            if cat not in categoryStats:
                categoryStats[cat] = 1
            else:
                categoryStats[cat] += 1
        context['jobCategories'] = {
            key: format(value/len(self.jobset)*100, '.2f') for key, value in categoryStats.items()
        }
        return context