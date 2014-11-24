from C4CApplication.meta import User, Message
from C4CApplication.models import Job, Member, Branch
from django.db.models import Max

class Visitor(User):
    
    def __init__(self, db_member):
        pass