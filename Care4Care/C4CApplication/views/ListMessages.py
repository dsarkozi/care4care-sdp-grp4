from C4CApplication.models import *
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView


from C4CApplication.views.utils import create_user
from C4CApplication.meta.user import User


class ListMessages(ListView):
    model = Message
    template_name = "C4CApplication/ListMessages.html"
    paginate_by = 5
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(ListMessages, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['received'] = self.received
        context['member'] = self.user
        return context
    
    def get(self, request, *args, **kwargs):
        self.received = kwargs['received']
        return super(ListMessages, self).get(request, *args, **kwargs)