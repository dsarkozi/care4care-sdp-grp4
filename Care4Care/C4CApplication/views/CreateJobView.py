from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from C4CApplication.views.forms.CreateJobForm import CreateJobForm
from C4CApplication.views.utils import create_user


class CreateJobView(FormView):
    template_name = "C4CApplication/CreateJob.html"
    form_class = CreateJobForm
    success_url = reverse_lazy('profile')
    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        self.user = create_user(self.request.session['email'])

        return super(CreateJobView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateJobView, self).get_form_kwargs()
        kwargs.update({'user' : self.user.db_member})
        return kwargs

    def form_valid(self, form):
        start_time = form.cleaned_data['start_time']
        duration = form.cleaned_data['duration']
        freq_dict = {
            '0' : '',
            '1' : form.cleaned_data['weekdays'],
            '2' : form.cleaned_data['dayrange']
        }
        recursive_day_list = freq_dict[form.cleaned_data['frequency']]
        status = self.user.create_job(
            branch_name=form.cleaned_data['branches'],
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            is_demand=self.kwargs['type'] == 'demand',
            frequency=form.cleaned_data['frequency'],
            category=form.cleaned_data['category'],
            visibility=form.cleaned_data['visibility'],
            date=form.cleaned_data['date'],
            start_time=start_time.hour*60 + start_time.minute,
            km=form.cleaned_data['km'],
            duration=duration.hour*60 + duration.minute,
            other_category=form.cleaned_data['other_category'],
            place=form.cleaned_data['place'],
            recursive_day=','.join(recursive_day_list)
        )
        if status:
            return super(CreateJobView, self).form_valid(form)
        else:
            return super(CreateJobView, self).form_invalid(form)

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
        # return super(CreateJobView, self).form_valid(form)