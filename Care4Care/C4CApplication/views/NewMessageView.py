from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from C4CApplication.views.forms.NewMessageForm import NewMessageForm
from C4CApplication.models import *
from C4CApplication.views.utils import create_user
from django.core.exceptions import PermissionDenied

from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy


class NewMessageView(FormView):
    model = Message
    template_name = 'C4CApplication/NewMessage.html'
    form_class = NewMessageForm
    success_url = reverse_lazy('newmessage')
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(NewMessageView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(NewMessageView, self).get_context_data(**kwargs)
        context['member'] = self.user.db_member
        context['connected'] = 'email' in self.request.session
        return context

    def form_valid(self, form):
        subject = form.cleaned_data['sujet']
        receiver = form.cleaned_data['receveur']
        message_content = form.cleaned_data['message']

        self.user.send_mail(self.user.db_member.mail, receiver, subject, message_content, 2)

        return super(NewMessageView, self).form_valid(form)