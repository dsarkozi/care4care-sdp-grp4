import abc


from C4CApplication.models import *


class User(object):
    __metaclass__ = abc.ABCMeta
    
    self.db_member = None
    
    
    
    ''' Si on veut mettre des methodes abstract
    
    @abc.abstractmethod
    def method_to_implement(self, input):
        """Method documentation"""
        return
        '''