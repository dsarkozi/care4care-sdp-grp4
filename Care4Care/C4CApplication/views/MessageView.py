from django.views.generic import DetailView
from C4CApplication.models import *
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user

class MessageView(DetailView):
   template_name = "C4CApplication/Message.html"  # chemin vers le template ˆ afficher
   context_object_name = "message"
   model = Message
   
   def dispatch(self, request, *args, **kwargs):
      if 'email' not in self.request.session:
         raise PermissionDenied  # HTTP 403
      self.user = create_user(self.request.session['email'])
      return super(MessageView, self).dispatch(request, *args, **kwargs)
    
   def get_context_data(self, **kwargs):
      context = super(MessageView, self).get_context_data(**kwargs)
      context['member'] = self.user.db_member
      context['connected'] = 'email' in self.request.session
      return context