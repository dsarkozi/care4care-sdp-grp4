from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy


class LogoutView(RedirectView):
    url = reverse_lazy("home")

    @never_cache
    def get(self, request, *args, **kwargs):

        if 'email' in request.session:  # If there is a member to log out

            if 'super_user_mail' in request.session:  # If it's a super user that was logged as another member

                request.session['email'] = request.session['super_user_mail']
                del request.session['super_user_mail']
                self.url = reverse_lazy("profile")

            else:  # If it's a simple lout out

                del request.session['email']
                self.url = reverse_lazy("home")

        return super(LogoutView, self).get(request, *args, **kwargs)