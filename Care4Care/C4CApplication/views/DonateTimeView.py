from django.views.generic.edit import FormView
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from C4CApplication.views.forms.DonateTimeForm import DonateTimeForm


class DonateTimeView(FormView):
    template_name = "C4CApplication/DonateTime.html"
    form_class = DonateTimeForm
    success_url = "processing/"

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(DonateTimeView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        context = super(DonateTimeView, self).get_context_data(**kwargs)
        context['donateTime'] = DonateTimeForm(auto_id=False)
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session
        return context