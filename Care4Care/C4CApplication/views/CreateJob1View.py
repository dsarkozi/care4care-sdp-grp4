from django.views.generic.edit import FormView

from C4CApplication.views.forms.CreateJob1Form import CreateJob1Form


class CreateJob1View(FormView):
    template_name = "C4CApplication/CreateJob1.html"
    form_class = CreateJob1Form
    success_url = "newjob2/"

    def get_context_data(self, **kwargs):
        context = super(CreateJob1View, self).get_context_data(**kwargs)
        context['NewJob1Form'] = CreateJob1Form(auto_id=False)
        return context