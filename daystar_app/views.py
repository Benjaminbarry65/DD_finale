from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SitterForm
from .models import Sitter
from django.urls import reverse
from django.template import loader

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
            location = form.cleaned_data['location'] 
            dob = form.cleaned_data['dob'] 
            gender = form.cleaned_data['gender'] 
            next_kin = form.cleaned_data['next_kin'] 
            nin = form.cleaned_data['nin']  
            recomm_name = form.cleaned_data['recomm_name']  
            religion = form.cleaned_data['religion']  
            level_education = form.cleaned_data['level_education']  
            contact = form.cleaned_data['contact'] 
            Sitter.objects.create(name=name, location=location, dob=dob, gender=gender, next_kin=next_kin, nin=nin, recomm_name=recomm_name, religion=religion, level_education=level_education, contact=contact) #duty=duty)
            return HttpResponseRedirect(reverse("sitter")) 
    else:
        form = SitterForm()
    sitterlist = Sitter.objects.all()     
    return render(request,'daystar_app/addsitter.html', {"sitterlist":sitterlist})


#create view for editsitter page
def editsitter(request, sitter_id):
    sitter = Sitter.objects.get(id=sitter_id)
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location'] 
            dob = form.cleaned_data['dob'] 
            gender = form.cleaned_data['gender'] 
            next_kin = form.cleaned_data['next_kin'] 
            nin = form.cleaned_data['nin']  
            recomm_name = form.cleaned_data['recomm_name']  
            religion = form.cleaned_data['religion']  
            level_education = form.cleaned_data['level_education']  
            contact = form.cleaned_data['contact']
            

         #updating fields in the database
            sitter.name = name
            sitter.location = location
            sitter.dob = dob
            sitter.gender = gender
            sitter.next_kin = next_kin
            sitter.nin = nin
            sitter.recomm_name = recomm_name
            sitter.religion = religion
            sitter.level_education = level_education
            sitter.contact = contact
            sitter.save()
            redirect_url = reverse('sitter')
            return HttpResponseRedirect(redirect_url)
    else:
        form = SitterForm(initial={'name':sitter.name, 'location':sitter.location, 'dob':sitter.dob, 'gender': sitter.gender, 'next_kin':sitter.next_kin, 'nin':sitter.nin, 'recomm_name':sitter.recomm_name, 'religion':sitter.religion, 'level_education':sitter.level_education, 'contact':sitter.contact})            
        return render(request,'daystar_app/editsitter.html', {'form': form, 'sitter_id': sitter_id})

#create view for delete
def deletesitter(request, sitter_id):
    Sitter.objects.filter(id=sitter_id).delete()
    redirect_url = reverse('sitter')
    return HttpResponseRedirect(redirect_url) 

#create view for view sitter page
def viewsitter(request, sitter_id):
    sitter = Sitter.objects.get(id=sitter_id)
    context = {'sitter': sitter}
    template = loader.get_template('daystar_app/viewsitter.html')
    return HttpResponse(template.render(context)) 

    #sitter = Sitter.objects.filter(id=sitter_id)
    #return render(request,'daystar_app/viewsitter.html', {'sitter_id': sitter_id})    
