from django.views.generic import DetailView
from C4CApplication.models.job import Job
from django import template
register = template.Library()

class JobDetailsView(DetailView):
    
    model = Job
    context_object_name = "job"
    template_name = "C4CApplication/jobdetails.html"

    def get_object(self):
        
        job = super(JobDetailsView, self).get_object()
    
        return job
    
    @register.filter
    def div( value, arg ):
        '''
        Divides the value; argument is the divisor.
        Returns empty string on any error.
        '''
        try:
            value = int( value )
            arg = int( arg )
            if arg: return value / arg
        except: pass
        return ''
    
    @register.tag('mod')
    def mod( value, arg ):
        '''
        Divides the value; argument is the divisor.
        Returns empty string on any error.
        '''
        try:
            value = int( value )
            arg = int( arg )
            if arg: return value % arg
        except: pass
        return ''