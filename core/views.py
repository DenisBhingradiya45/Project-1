from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.contrib import messages
from django.views.generic import ListView
from django.template import loader




# Create your views here.

def Home(request):
    blog = Blog_Model.objects.all()
    return render(request, "Home.html", {'blog':blog})

def SignUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                messages.success(request, "Account Created ")
                fm.save()
                return HttpResponseRedirect('/Home/')
        else:
            fm = SignUpForm()
        return render(request, "Sign-Up.html", {"form":fm})
    else:
        return HttpResponseRedirect('/Home/')

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
                    return HttpResponseRedirect('/Home/')
                else:
                    messages.info(request, 'Try again! username or password is incorrect')
        else:
            fm = AuthenticationForm()
        return render(request, "Sign-In.html", {"form":fm})
    else:
        return HttpResponseRedirect('/Home/')

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/Home/')

def Profile(request):
    if request.user.is_authenticated:
        pro = User.objects.all()
        return render(request, 'Profile.html', {'pro':pro})
    else:
        return HttpResponseRedirect('/Sign-In/')

def AddBlog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            discription = request.POST['content']
            user = User.objects.get(username=(request.user.username))
            author = user
            image = request.FILES['upload']
            if Blog_Model.objects.filter(title=title).exists():
                messages.error(request, "This Bolg Is Alredy Uploaded!!")
            else:
                Blog_Model.objects.create(title=title, discription=discription, author=author, image=image)
                return redirect('/UserBlog/')

        return render(request, "Add-Blog.html")
    else:
        return HttpResponseRedirect('/SignIn/')

def UpdateBlog(request, pk):
    if request.user.is_authenticated:
        fm = get_object_or_404(Blog_Model, pk=pk)
        if request.method == 'POST':
            fm.title = request.POST.get('title')
            fm.discription = request.POST.get('content')
            if request.FILES.get('image'):
                fm.image = request.FILES['image']
            fm.save()
            return redirect('/UserBlog/')   
        return render(request, 'Update-Blog.html', {'fm': fm})
    else:
        return HttpResponseRedirect('/SignIn/')



def DeleteBlog(request, pk):
    if request.user.is_authenticated:
        fm = Blog_Model.objects.get(pk=pk)
        if request.user == fm.author:
            Blog_Model.objects.filter(pk=pk).delete()
            return redirect('/UserBlog/')
    else:
        return HttpResponseRedirect('/SignIn/')

def BlogDetails(request, id):
    item = Blog_Model.objects.get(id=id)
    return render(request,'Blog-Details.html', {'item': item})

def UserBlog(request):
    user = User.objects.get(username=(request.user.username))
    posts = Blog_Model.objects.filter(author=user)
    context = {'user': user, 'posts': posts}
    return render(request, 'User-Blog.html', context)

def AboutUs(request):
    return render(request, "About-Us.html")
