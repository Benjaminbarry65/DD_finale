from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.homeindex, name='home'),
    path('abouts', views.aboutindex, name='about'),
    path('contacts', views.contactindex, name='contact')
]