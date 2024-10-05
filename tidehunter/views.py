from django.shortcuts import render

# Create your views here.
def forum(request):
    return render(request, template_name="home/forum.html")

def registration(request):
    return render(request, template_name="registration.html")