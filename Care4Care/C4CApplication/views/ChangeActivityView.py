from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from django.views.generic import TemplateView


class ChangeActivityView(TemplateView):
    template_name = "C4CApplication/ChangeActivity.html"
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(FavoritesView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ChangeActivityView, self).get_context_data(**kwargs)
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session
        return context