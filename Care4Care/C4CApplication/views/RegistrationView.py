from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from C4CApplication.views.forms.RegistrationForm import RegistrationForm


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = "C4CApplication/Registration.html"
    success_url = reverse_lazy('home')