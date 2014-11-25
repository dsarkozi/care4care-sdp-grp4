from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from C4CApplication.models import *
from django.contrib.sessions.models import Session

# Pour l'admin
# Register your models here.

class SessionAdmin(ModelAdmin):
    @staticmethod
    def _session_data(obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

admin.site.register(Session, SessionAdmin)

admin.site.register(Branch)
admin.site.register(Member)
admin.site.register(Job)
admin.site.register(Message)