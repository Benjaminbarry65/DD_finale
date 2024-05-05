from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SitterForm
from .models import Sitter
from django.urls import reverse

# Create your views here.
#create view for sitter page
def sitter_home(request):
    form = SitterForm()
    sitterlist = Sitter.objects.all()
    return render(request,'daystar_app/sitter.html', {'sitterlist':sitterlist})


#create view for addsitter page
def addsitter(request):
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            #date_admitted = form.cleaned_data['date_admitted']
            contact = form.cleaned_data['contact']
            #duty = form.cleaned_data['duty']
            Sitter.objects.create(name=name, gender=gender, contact=contact) #date_admitted=date_admitted, duty=duty)
            return HttpResponseRedirect(reverse("sitter")) 
    else:
        form = SitterForm()
        sitterlist = Sitter.objects.all()     
        return render(request,'daystar_app/addsitter.html', {"sitterlist":sitterlist, "form":form})


#create view for editsitter page
def editsitter(request, sitter_id):
    sitter = Sitter.objects.get(id=sitter_id)
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender'] 
            #date_admitted = form.cleaned_data['date_admitted'] 
            contact = form.cleaned_data['contact'] 
            #duty = form.cleaned_data['duty']

         #updating fields in the database
            sitter.name = name
            sitter.gender = gender
            sitter.contact = contact
            sitter.save()
            redirect_url = reverse('sitter')
            return redirect(redirect_url)
    else:
        form = SitterForm(initial={'name': sitter.name, 'gender': sitter.gender, 'contact': sitter.contact})            
        return render(request,'daystar_app/editsitter.html', {'form': form, 'sitter_id': sitter_id})

#create view for delete
def deletesitter(request, sitter_id):
    Sitter.objects.filter(id=sitter_id).delete()
    redirect_url = reverse('sitter')
    return HttpResponseRedirect(redirect_url) 
