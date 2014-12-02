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
        context['createJob'] = CreateJobForm(user=self.user.db_member, auto_id=False)
        context['member'] = self.user.db_member
        return context

    # def form_invalid(self, form):
    #     branches = form.cleaned_data['branches']
    #     print(branches)
    #     print('all' in branches)
    #     return super(CreateJobView, self).form_invalid(form)

    def form_valid(self, form):
        #TODO Call to create_job
        # self.user.create_job(
        #     is_demand=(self.kwargs['type'] == 'demand'),
        #     comment=form.cleaned_data['desc'],
        #
        # )
        # branches = form.cleaned_data['branches']
        # if 'all' in branches:
        #     branches.remove('all')
        # for branch in branches:
        #     self.user.create_job(
        #         branch_name=branch,
        #         date=form.cleaned_data['']
        #     )
        return super(CreateJobView, self).form_valid(form)