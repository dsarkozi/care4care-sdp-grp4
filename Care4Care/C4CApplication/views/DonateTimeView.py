from django.views.generic.edit import FormView

from C4CApplication.views.forms.DonateTimeForm import DonateTimeForm


class DonateTimeView(FormView):
    template_name = "C4CApplication/DonateTime.html"
    form_class = DonateTimeForm
    success_url = "processing/"

    def get_context_data(self, **kwargs):
        context = super(DonateTimeView, self).get_context_data(**kwargs)
        context['donateTime'] = DonateTimeForm(auto_id=False)
        return context