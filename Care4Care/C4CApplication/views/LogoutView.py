from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView

class LogoutView(RedirectView):
    url = "/"

    @never_cache
    def get(self, request, *args, **kwargs):
        del request.session['email']
        return super(LogoutView, self).get(request, *args, **kwargs)