from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name="home_page"),
    path('login/', views.login, name="login_page"),
    path('singup/', views.signup, name="signup_page"),
    path('offer/', views.offer, name="offer_page"),
    path('ride/', views.ride, name="ride_page"),
]
