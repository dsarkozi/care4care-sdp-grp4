from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.models.member import Member
from C4CApplication.views.utils import create_user
from C4CApplication.meta.user import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


class ChangeActivityRedirectView(RedirectView):

    
    url = reverse_lazy("myc4c")
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(ChangeActivityRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        active = kwargs['active']
        self.user.change_status(active)
        return super(ChangeActivityRedirectView, self).get(request, *args, **kwargs)