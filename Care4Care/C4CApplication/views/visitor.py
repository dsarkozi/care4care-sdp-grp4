from C4CApplication.views import User, Message
from C4CApplication.models import Job, Member, Branch
from django.db.models import Max

class Visitor(user):
    
    def __init__(self, db_member):
        pass