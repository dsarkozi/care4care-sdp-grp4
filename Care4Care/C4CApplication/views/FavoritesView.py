from C4CApplication.models.member import Member
from django.views.generic.edit import FormView
from C4CApplication.views.forms.FavIgnForm import FavIgnForm
from django.core.urlresolvers import reverse_lazy
from C4CApplication.views.utils import create_user
from C4CApplication.meta.user import User
from django.core.exceptions import PermissionDenied
    

class FavoritesView(FormView):
    template_name = "C4CApplication/Favorites.html"
    form_class = FavIgnForm
    success_url = reverse_lazy("favorites")
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(FavoritesView, self).dispatch(request, *args, **kwargs)
 
    def get_context_data(self, **kwargs):
        context = super(FavoritesView, self).get_context_data(**kwargs)
        context['favIgnForm'] = FavIgnForm()
        context['member'] = self.user.db_member
        return context
    
    def form_valid(self, form):
        favorite_mail = form.cleaned_data['email']
        self.user.add_favorite(favorite_mail)
        
        return super(FavoritesView, self).form_valid(form)