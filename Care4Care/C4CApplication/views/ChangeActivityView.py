from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from django.views.generic import TemplateView


class ChangeActivityView(TemplateView):
    template_name = "C4CApplication/ChangeActivity.html"