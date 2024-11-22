from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def home(request):
    post=Post.objects.all()
    context={
        'post':post,
    }
    return render(request,template_name="Home/home.html",context=context)
def clubdetails(request):
    club=Club.objects.all()
    context={
        'club':club,
    }
    return render(request,template_name="Home/clubdetails.html",context=context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('name')  
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  

    return render(request, template_name="register/login.html")

# Signup Page
def signup(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return redirect('signup')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')  

    return render(request, template_name="register/signup.html")

@login_required
def createpost(request):
    return render(request,template_name="Home/createpost.html")

def resources(request):
    resource=Resources.objects.all()
    context={
        'resource':resource
    }
    return render(request,template_name="Home/resources.html",context=context)

def forum(request):
    forum=Forum.objects.all()
    context={
        'forum':forum
    }
    return render(request,template_name="Home/forum.html",context=context)
