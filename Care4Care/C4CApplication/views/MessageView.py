from django.views.generic import DetailView
from C4CApplication.models import *

class MessageView(DetailView):
   template_name = "C4CApplication/viewMessage.html"  # chemin vers le template ˆ afficher
   context_object_name = "message"
   model = Message