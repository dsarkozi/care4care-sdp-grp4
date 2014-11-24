from django.shortcuts import render
from django.http import HttpResponse
from C4CApplication.models import Member
from C4CApplication import models

# Create your views here.

def home(request):
    return HttpResponse("Hello world !")

def profile(request):
    member = Member()
    
    member.mail = 'armand.bosquillon@gmail.com'
    member.password = 'test'
    member.first_name = 'armand'
    member.last_name = 'bosquillon'
    member.birthday = '1993-11-05'
    #member.tag = 
    member.mobile = '026785095'
    member.telephone = '0475643865'
    member.register_date = '2014-02-02'
    member.address = 'rixensart'
    #member. =
    
    member.save()
    
    return render(request, 'C4CApplication/profile.html', {'member':member})