from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    occupation = models.TextField(max_length=50, default='No Occupation mentioned')
    phone = models.TextField(max_length=12, default='No phone no. provided')

