from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('SignUp/', SignUp, name="SignUp"),
    path('SignIn/', SignIn, name="SignIn"),
    path('LogOut/', LogOut, name="LogOut"),
    path('home/', home, name="home"),
    path('about/', about_us, name="about_us"),
    path('BlogDetails/', BlogDetails, name="BlogDetails"),
    path('Profile/', Profile, name="Profile"),

]

urlpatterns += staticfiles_urlpatterns()