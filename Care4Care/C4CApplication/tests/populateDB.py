from django.test import TestCase
from C4CApplication.models import *

b = Branch()
b.name = "Nivelles"
b.town = "Nivelles"
b.save()