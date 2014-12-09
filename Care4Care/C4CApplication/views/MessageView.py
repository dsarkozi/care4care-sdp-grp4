from django.views.generic import DetailView
from C4CApplication.models import *
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from C4CApplication.models.mailbox import Mailbox

class MessageView(DetailView):
    template_name = "C4CApplication/Message.html"  # path to the template to display
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
       
       message = context['message']
       mailbox = Mailbox.objects.filter(member_receiver=self.user.db_member, message=message)
       if len(mailbox) != 1 :
           print("problem, da !")
       mailbox = mailbox[0]
       mailbox.status = True
       mailbox.save()
        
       return context