from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#create view for the landing page
def index(request):
    return render(request, 'home_app/index.html')

#create view for the home page
def homeindex(request):
    return render(request, 'home_app/home.html')

#create view for the about page
def aboutindex(request):
    return render(request, 'home_app/about.html')

#create view for the contact page
def contactindex(request):
    return render(request, 'home_app/contact.html')

#create view for the login page
def loginindex(request):
    return render(request, 'registration/login.html')    