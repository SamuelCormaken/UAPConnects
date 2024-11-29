from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required
def home(request):
    post=Post.objects.all()
    context={
        'post':post,
    }
    return render(request,template_name="Home/home.html",context=context)

@login_required
def createpost(request):
    post=Post.objects.all()
    context={
        'post':post,
    }
    return render(request,template_name="Home/createpost.html",context=context)

def forum(request):
    forum=Forum.objects.all()
    context={
        'forum':forum
    }
    return render(request,template_name="Home/forum.html",context=context)

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


#upload post(Create) 
@login_required
def upload_post(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('home')
    context={'form':form}
    return render(request,template_name="allforms\postform.html",context=context)

def update_post(request,id):
    post=Post.objects.get(pk=id)
    form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('home')
    context={'form':form}
    return render(request,template_name="allforms\postform.html",context=context)

def delete_post(request,id):
    post=Post.objects.get(pk=id)
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render(request,template_name="allforms/delete_post.html")

@login_required
def upload_query(request):
    form=ForumPost_Form()
    if request.method=='POST':
        form=ForumPost_Form(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('forum')
    context={'form':form}
    return render(request,template_name="allforms\postform.html",context=context)

def update_query(request,id):
    forum=Forum.objects.get(pk=id)
    form=ForumPost_Form(instance=forum)
    if request.method=='POST':
        form=ForumPost_Form(request.POST,request.FILES,instance=forum)
        if form.is_valid():
            forum=form.save(commit=False)
            forum.user=request.user
            forum.save()
            return redirect('forum')
    context={'form':form}
    return render(request,template_name="allforms\postform.html",context=context)

def delete_query(request,id):
    forum=Forum.objects.get(pk=id)
    if request.method=='POST':
        forum.delete()
        return redirect('forum')
    return render(request,template_name="allforms/delete_query.html")

def resources(request):
    resource=Resources.objects.all()
    context={
        'resource':resource
    }
    return render(request,template_name="Home/resources.html",context=context)


def upload_resource(request):
    form = Resource_Form()
    if request.method == 'POST':
        form = Resource_Form(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('resources')
    context = {'form':form}
    return render(request, template_name='allforms/resourceform.html',context=context)

def update_resource(request,id):
    resource = Resources.objects.get(pk=id)
    form = Resource_Form(instance=resource)
    if request.method=='POST':
        form = Resource_Form(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            resource=form.save(commit=False)
            resource.user=request.user
            resource.save()
            return redirect('resources')
    context = {'form':form}
    return render(request,template_name='allforms/resourceform.html', context=context)

def delete_resource(request,id):
    resource = Resources.objects.get(pk=id)
    if request.method == 'POST':
        resource.delete()
        return redirect('resources')
    return render(request,template_name='allforms/deleteresource.html')



    
