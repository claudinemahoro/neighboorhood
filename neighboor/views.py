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
def create_hood(request):
    if request.method == 'POST':
        form = NeighborForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user
            hood.save()
            return redirect('welcome')
    else:
        form = NeighborForm()
    return render(request, 'hood.html', {'form': form})
@login_required(login_url='/accounts/login/')
def new_post(request):
    newpost = Post.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('hood')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form, "newpost": newpost})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form1 = BusinessForm(request.POST, request.FILES)
        if form1.is_valid():
            bus = form1.save(commit=False)
            bus.user = current_user
            bus.save()
        return redirect('hood')

    else:
        form1 = BusinessForm()
    return render(request, 'new_business.html', {"form1": form1})
