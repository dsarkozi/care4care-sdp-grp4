from django.contrib import admin

from C4CApplication.models import *


# Pour l'admin
# Register your models here.
admin.site.register(Branch)
admin.site.register(Member)
admin.site.register(Job)
admin.site.register(Message)