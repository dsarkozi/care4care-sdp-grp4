from django.core.exceptions import PermissionDenied
from django.db.models.aggregates import Avg, Sum
from django.views.generic.base import TemplateView
import time
from C4CApplication.models.job import Job
from C4CApplication.models.member import Member
from C4CApplication.views.utils import create_user


class AccountStatsView(TemplateView):
    template_name = "C4CApplication/AccountAndStats.html"
    user = None
    jobset = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])
        # self.jobset = Job.objects.filter(mail=self.request.session['email'])     #TODO Change this with db_member.job
        self.jobset = self.user.db_member.job.all()
        return super(AccountStatsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AccountStatsView, self).get_context_data(**kwargs)
        # General info
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session
        context['jobAmount'] = self.jobset.count()
        context['jobAverageTime'] = time.strftime('%H:%M:%S', time.gmtime(self.jobset.aggregate(Avg('duration'))['duration__avg']))
        context['jobTotalDistance'] = self.jobset.aggregate(Sum('km'))['km__sum']
        context['jobCategories'] = self.categoryStats(self.jobset)

        # Help received
        context['helpedDone'] = self.queryset2list(
            self.jobset.filter(type=True, done=True).order_by('-date')
        )
        context['helpedPending'] = self.queryset2list(
            self.jobset.filter(type=True, done=False).order_by('-date')
        )

        # Help given
        context['helperDone'] = self.queryset2list(
            self.jobset.filter(type=False, done=True).order_by('-date')
        )
        context['helperPending'] = self.queryset2list(
            self.jobset.filter(type=False, done=False).order_by('-date')
        )

        return context

    @staticmethod
    def queryset2list(queryset):
        dictlist = list()
        for item in queryset:
            dictlist += [{
                'id' : item.id,
                'date' : item.date,
                'category' : Job.CAT_DICT[item.category],
                'duration' : item.duration,
                'whom' : str(Member.objects.filter(mail=item.mail)[0]),
                'km' : item.km,
            }]
        return dictlist

    @staticmethod
    def categoryStats(jobset):
        categoryStats = dict()
        for job in jobset:
            cat = job.CAT_DICT[job.category]
            if cat not in categoryStats:
                categoryStats[cat] = 1
            else:
                categoryStats[cat] += 1
        return {
            key: format(value/len(jobset)*100, '.2f') for key, value in categoryStats.items()
        }