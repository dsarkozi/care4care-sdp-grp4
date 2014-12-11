from django.views.generic.list import ListView

from C4CApplication.models.job import Job


class JobSearchView(ListView):
    queryset = Job.objects.all()
    model = Job
    paginate_by = 10
    context_object_name = 'jobs'
    template_name = 'C4CApplication/JobSearch.html'