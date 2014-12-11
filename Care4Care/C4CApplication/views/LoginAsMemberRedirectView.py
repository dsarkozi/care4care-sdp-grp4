from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy

from C4CApplication.views.utils import create_user


class LoginAsMemberRedirectView(RedirectView):

    url = reverse_lazy("profile")
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(LoginAsMemberRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        mail_member = kwargs['mail']
        self.user.log_as_member(mail_member, self.request.session)
        return super(LoginAsMemberRedirectView, self).get(request, *args, **kwargs)