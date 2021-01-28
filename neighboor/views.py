from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse
import datetime as dt 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def welcome(request):
    new = NeighbourHood.objects.all()
    return render(request, 'welcome.html', { "new": new})

def hoods(request):
     new = NeighbourHood.objects.all()
     newpost = Post.objects.all()
     business = Business.objects.all()
     return render(request, 'all.html', {"new": new, "newpost":newpost, "business":business})  

@login_required(login_url='/accounts/login')
def hood_details(request,neighbour_id):
     details=NeighbourHood.get_specific_hood(neighbour_id)

     return render(request,'all.html',{"details":details})
@login_required(login_url='/accounts/login')
def bus_details(request,business_id):
     details1=Business.get_specific_bus(business_id)

     return render(request,'new_business.html',{"details1":details1})
