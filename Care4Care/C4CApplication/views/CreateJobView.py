from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormView

from C4CApplication.views.forms.CreateJobForm import CreateJobForm
from C4CApplication.views.utils import create_user


class CreateJobView(FormView):
    template_name = "C4CApplication/CreateJob.html"
    form_class = CreateJobForm
    success_url = "processing/"
    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])

        return super(CreateJobView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateJobView, self).get_context_data(**kwargs)
        context['createJob'] = CreateJobForm(auto_id=False)
        return context

    def form_valid(self, form):
        #TODO Call to create_job
        # self.user.create_job(
        #     is_demand=(self.kwargs['type'] == 'demand'),
        #     comment=form.cleaned_data['desc'],
        #
        # )

        return super(CreateJobView, self).form_valid(form)