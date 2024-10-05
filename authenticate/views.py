from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name="Home/Home.html")
def forum(request):
    return render(request,template_name="Home/Forum.html")
def login(request):
    return render(request,template_name="login.html")
