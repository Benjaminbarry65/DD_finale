from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages



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

#create view for the reg page
def reguser(request):
    if request.method == 'POST':
        reguserForm = RegForm(request.POST)
        if reguserForm.is_valid():
            reguserForm.save()
            username = reguserForm.cleaned_data['username']
            raw_password = reguserForm.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.info(request, 'Please fill form correctly')
    else:
        reguserForm = RegForm()
    return render(request, 'registration/reg.html', {'reguserForm': reguserForm})


#create view for the login page
def loginindex(request):
    if request.method == 'POST':
        logform = LoginForm(request.POST)
        if logform.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.info(request, 'Please fill form correctly')
        else:
            messages.info(request, 'you have input invalid information')
    else:
        logform = LoginForm()
    return render(request, 'registration/login.html', {'logform': logform})    


#create logout view    
def logoutuser(request):
    logout(request)
    return redirect('index')
    #return HttpResponseRedirect(reverse('index'))