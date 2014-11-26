from C4CApplication.models import *
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView




class ListMessages(ListView):
    model = Message
    template_name = "C4CApplication/ListMessages.html"
    paginate_by = 5
    
    