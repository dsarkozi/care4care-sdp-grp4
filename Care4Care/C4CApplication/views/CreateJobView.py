from django.views.generic.edit import FormView

from C4CApplication.views.forms.CreateJobForm import CreateJobForm


class CreateJobView(FormView):
    template_name = "C4CApplication/CreateJob.html"
    form_class = CreateJobForm
    success_url = "processing/"

    def get_context_data(self, **kwargs):
        context = super(CreateJobView, self).get_context_data(**kwargs)
        context['createJob'] = CreateJobForm(auto_id=False)
        return context