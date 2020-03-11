from django.contrib import admin
from .models import UserProfile
from .models import offermodel


admin.site.register(UserProfile)
admin.site.register(offermodel)