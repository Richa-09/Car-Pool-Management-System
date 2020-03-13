from django.contrib import admin
from .models import UserProfile
from .models import offermodel, rideReq


admin.site.register(UserProfile)
admin.site.register(offermodel)
admin.site.register(rideReq)