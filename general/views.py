from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, offermodel
from .forms import OfferForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'general/home.html')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            messages.info(request,"Username/Password invalid")
            return render(request,'general/login.html')
    return render(request,'general/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        phone = request.POST['phone']
        occupation = request.POST['occupation']
        try:
            user=User.objects.get(username=name)
        except:
            if pwd1 != pwd2:
              messages.info(request,"Password don't match")
              return render(request,'general/signup.html')
            if len(pwd1)<8:
                messages.info(request,"Password is too short")
                return render(request,'general/signup.html')
            us = User()
            us.username = name
            us.email = email
            us.set_password(pwd1)
            us.save()

            p=UserProfile()
            user = User.objects.get(username=name)
            p.user = user
            p.occupation = request.POST['occupation'] 
            p.phone = request.POST['phone']
            p.save()

            messages.success(request,"Signed up successfully")
            return redirect('login_page')
        else :
            messages.info(request,"Username already exists")
            return render(request,'general/signup.html')
    return render(request,'general/signup.html')
            
               
@login_required(login_url='login_page')
def offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)

        if form.is_valid():
            of = offermodel()
            of.destination1 = form.cleaned_data['destination1']
            of.destination2 = form.cleaned_data['destination2']
            of.carModel = form.cleaned_data['carModel']
            of.seatsAvailable = form.cleaned_data['seatsAvailable']
            of.cost = form.cleaned_data['cost']
            of.date = form.cleaned_data['date']
            of.time = form.cleaned_data['time']
            of.name = request.user
            of.save()
            messages.success(request," Successfully done, let's wait for requests!")
            return render(request,'general/home.html',{
                'form':form
            })
    else:
        form =OfferForm()
    return render(request,'general/offer.html',{
        'form':form
    })
def ride(request):
    return render(request,'general/ride.html')

def logoutUser(request):
    logout(request)
    return render(request,'general/home.html')

def profile(request):
    return render(request,'general/profile.html')