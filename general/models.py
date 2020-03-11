from django.db import models
from django.contrib.auth.models import User
from django import forms

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    occupation = models.TextField(max_length=50, default='No Occupation mentioned')
    phone = models.TextField(max_length=12, default='No phone no. provided')
    

class offermodel(models.Model):
    destination1 = models.CharField(max_length=100)
    destination2 = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    carModel = models.CharField(max_length=40)
    seatsAvailable = models.IntegerField()
    cost = models.IntegerField(default=0)
    name = models.TextField(max_length=30, default='no name')

