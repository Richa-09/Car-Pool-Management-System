from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name="home_page"),
    path('login/', views.loginUser, name="login_page"),
    path('signup/', views.signup, name="signup_page"),
    path('offer/', views.offer, name="offer_page"),
    path('ride/', views.ride, name="ride_page"),
    path('logout/', views.logoutUser, name="logout_page"),
    path('profile/', views.profile, name="profile_page"),
]
