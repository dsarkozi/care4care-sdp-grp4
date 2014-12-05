from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormView
from C4CApplication.models.member import Member
from C4CApplication.models.branch import Branch

from C4CApplication import models
from django.core.urlresolvers import reverse_lazy
from C4CApplication.meta.user import User
from C4CApplication.views.forms.SearchForm import SearchForm
from C4CApplication.views.utils import create_user


class SearchJobView(FormView):
    template_name = "C4CApplication/SearchJob.html"
    form_class = SearchForm
    success_url = reverse_lazy("searchjob")  # Stay on the same page
    user = None

    show_demands = False
    filter_member_mail = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(SearchJobView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchJobView, self).get_context_data(**kwargs)

        job_list = self.user.get_visible_job_list(show_demands=self.show_demands)
        filtered_job_list = []
        for job in job_list:
            # We show only jobs that are not yet accepted and filter following the preference that are entered
            if not job.accepted and (SearchJobView.filter_member_mail is None or SearchJobView.filter_member_mail == job.mail):
                filtered_job_list.append(job)

        context['job_list'] = filtered_job_list

        context['searchform'] = SearchForm(auto_id=False,
                                           data={'type_of_job': 'demand' if SearchJobView.show_demands else 'offer',
                                                 'email_member': '' if SearchJobView.filter_member_mail is None
                                                                    else SearchJobView.filter_member_mail})

        return context

    def form_valid(self, form):
        show_demands = form.cleaned_data['type_of_job']
        filter_member_mail = form.cleaned_data['email_member']

        SearchJobView.show_demands = show_demands == "demand"

        member = models.Member.objects.filter(mail=filter_member_mail)

        if len(member) == 0 or member[0].deleted:  # if member not found, we do not filter
            SearchJobView.filter_member_mail = None
        else:
            SearchJobView.filter_member_mail = filter_member_mail

        return super(SearchJobView, self).form_valid(form)