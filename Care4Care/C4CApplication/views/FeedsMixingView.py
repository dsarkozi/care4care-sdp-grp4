from django.views.generic.list import MultipleObjectMixin
from C4CApplication.models.job import Job
from _decimal import Context

class FeedsMixingView(MultipleObjectMixin):
    
  context_object_name = 'feed_list'
  object_list = None
  # Returns a dictionary. (NB: "**", stars are use by convention)  
  def get_context_data(self, **kwargs):
    """
    Get the context for this view.
    """
    context = super(FeedsMixingView, self).get_context_data(**kwargs)
    self.object_list = context['feed_list']
    
    # Pour trier par date, on doit implémenter une classe Meta...
    offer_list = Job.objects.filter(type=False)
    demand_list = Job.objects.filter(type=True)
    
    if len(offer_list)>= 10:
        offer_list = offer_list[0:10]
    if len(demand_list)>=10:
        demand_list = demand_list[0:10]
    
    context['offer_list'] = offer_list
    context['demand_list'] = demand_list
    return context

