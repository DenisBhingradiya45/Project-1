from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.contrib import messages



# Create your views here.

def home(request):
    blog = Blog_Model.objects.all()
    return render(request, "home.html", {'blog':blog})

def SignUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/home/')
        else:
            fm = SignUpForm()
        return render(request, "register.html", {"form":fm})
    else:
        return HttpResponseRedirect('/home/')

def SignIn(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    messages.info(request, 'Try again! username or password is incorrect')
        else:
            fm = AuthenticationForm()
        return render(request, "signin.html", {"form":fm})
    else:
        return HttpResponseRedirect('/home/')

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def profile(request):
    pr = User.objects.all()
    return render(request, 'profile.html', {'pr':pr})

def AddBlog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            title = request.POST['title']
            discription = request.POST['discription']
            author = request.user.username
            image = request.FILES['upload']
            if Blog_Model.objects.filter(title=title).exists():
                messages.error(request, "aaaaaaaaaaaaaaa")
            else:
                Blog_Model.objects.create(title=title, discription=discription, author=author, image=image)

        return render(request, "AddBlog.html")
    else:
        return HttpResponseRedirect('/SignIn/')
    
def BlogDetails(request):
    return render(request, "blog_detail.html")

def about_us(request):
    return render(request, "about_us.html")

