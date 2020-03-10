from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'general/home.html')

def login(request):
    return render(request,'general/login.html')

def signup(request):
    return render(request,'general/signup.html')

def offer(request):
    return render(request,'general/offer.html')

def ride(request):
    return render(request,'general/ride.html')
