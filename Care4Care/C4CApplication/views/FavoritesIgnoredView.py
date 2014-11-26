from django.views.generic.edit import FormView
from C4CApplication.views.forms.FavIgnForm import FavIgnForm

class FavoritesIgnoredView(FormView):
    template_name = "C4CApplication/FavoritesIgnored.html"
    form_class = FavIgnForm
 
    def get_context_data(self, **kwargs):
        context = super(FavoritesIgnoredView, self).get_context_data(**kwargs)
        context['favIgnForm'] = FavIgnForm()
        return context

    def form_valid(self, form):
        email = form.cleaned_data['email']
        return super(FavoritesIgnoredView, self).form_valid(form)

