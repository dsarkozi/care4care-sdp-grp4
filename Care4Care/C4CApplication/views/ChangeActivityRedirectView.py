from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

from C4CApplication.views.utils import create_user


class ChangeActivityRedirectView(RedirectView):

    url = None
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(ChangeActivityRedirectView, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        self.url = reverse("profile")
        return self.url

    @never_cache
    def get(self, request, *args, **kwargs):
        active = kwargs['active']
        self.user.change_status(active)
        return super(ChangeActivityRedirectView, self).get(request, *args, **kwargs)