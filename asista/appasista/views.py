from __future__ import unicode_literals
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


# Create your views here.

def index(request):
    return HttpResponse("haiiii new project")

def link(request, pid):
    pp = Product.objects.filter(p_id = pid)
    for i in pp:
        uu = User.objects.filter(id = i.manfac_id)
    return render(request,'appasista/link.html',{'pp' : pp, 'uu' : uu},)
    
def flink(request, pid):
    pp = Product.objects.filter(p_id = pid)
    for i in pp:
        uu = User.objects.filter(id = i.manfac_id)
    return render(request,'appasista/flink.html',{'pp' : pp,'uu' : uu},)

def first(request):
    productDetails = Product.objects.all()
    return render(request, 'appasista/first.html', {'productDetails' : productDetails},)

def manufacturer(request):
    return render(request, 'appasista/manufacturer.html', {})
    
def launch(request):
    return render(request, 'appasista/launch.html', {})

def funder(request):
    productDetails = Product.objects.filter(fund_or_sell = "fund")[:4]
    pd = Product.objects.filter(fund_or_sell = "fund")[4:8]
    pd1 = Product.objects.filter(fund_or_sell = "fund")[8:12]
    return render(request, 'appasista/funder.html', {'productDetails' : productDetails, 'pd' : pd, 'pd1' : pd1},)

def customer(request):
    productDetails = Product.objects.filter(fund_or_sell = "sell")[:4]
    pd = Product.objects.filter(fund_or_sell = "sell")[4:8]
    pd1 = Product.objects.filter(fund_or_sell = "sell")[8:12]
    return render(request, 'appasista/customer.html', {'productDetails' : productDetails, 'pd' : pd, 'pd1' : pd1},)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'appasista/launch.html', {})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

    
def Saved(request):
    return render(request, 'appasista/Saved.html', {})

def manufacturer_addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            p_id = form.cleaned_data['p_id']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            unitcost = form.cleaned_data['unitcost']
            fund_or_sell = form.cleaned_data['fund_or_sell']
            video_url = form.cleaned_data['video_url']
            manfac_id = request.user.id
            f = Product(p_id = p_id, name = name, description = description, image = image,unitcost = unitcost, fund_or_sell = fund_or_sell, video_url = video_url, manfac_id = manfac_id)
            f.save()
            return render(request, 'appasista/manufacturer.html', {})
    else:
        form = ProductForm()
    return render(request, 'appasista/manufacturer_addproduct.html', {'form':form})  

def home(request):
    return render(request, 'appasista/home.html', {})
@login_required    
def home_h(request):
    return render(request, 'appasista/home_h.html', {})
    
def added_products(request):
    productDetails = Product.objects.filter(manfac_id = request.user.id)[:4]
    pd = Product.objects.filter(manfac_id = request.user.id)[4:8]
    pd1 = Product.objects.filter(manfac_id = request.user.id)[8:12]
    return render(request, 'appasista/added_products.html', {'productDetails' : productDetails, 'pd' : pd, 'pd1' : pd1},)

