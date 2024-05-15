from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.template import loader

# Create your views here.
#create views for baby page
def babyhome(request):
    #form = BabyForm()
    babylist = Baby.objects.all()
    return render(request, 'baby_app/baby.html', {'babylist': babylist})

#create view to add baby page
def addbaby(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        print(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            location = form.cleaned_data['location']
            name_dropper = form.cleaned_data['name_dropper']
            time_arrival = form.cleaned_data['time_arrival']
            name_parents = form.cleaned_data['name_parents']
            amount_paid = form.cleaned_data['amount_paid']
            period_stay = form.cleaned_data['period_stay']
            #baby_number = form.cleaned_data['baby_number']
            Baby.objects.create(name=name, gender= gender, age=age, location=location, name_dropper=name_dropper, time_arrival=time_arrival, name_parents=name_parents, amount_paid=amount_paid, period_stay=period_stay) #baby_number=baby_number)
            return HttpResponseRedirect(reverse("baby"))
    else:
        form = BabyForm()
    babylist = Baby.objects.all()    
    return render(request, 'baby_app/addbaby.html', {'babylist': babylist})

#create view to edit baby page
def editbaby(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender'] 
            age = form.cleaned_data['age']
            location = form.cleaned_data['location']
            name_dropper = form.cleaned_data['name_dropper']
            time_arrival = form.cleaned_data['time_arrival']
            name_parents = form.cleaned_data['name_parents']
            amount_paid = form.cleaned_data['amount_paid']
            period_stay = form.cleaned_data['period_stay']
            #baby_number = form.cleaned_data['baby_number']

          #updating fields in the database
            baby.name = name
            baby.gender = gender
            baby.age = age
            baby.location = location
            baby.name_dropper = name_dropper
            baby.time_arrival = time_arrival
            baby.name_parents = name_parents
            baby.amount_paid = amount_paid
            baby.period_stay = period_stay
            #baby.baby_number =baby_number
            baby.save()
            redirect_url = reverse('baby')
            return HttpResponseRedirect(redirect_url)
    else:
        form = BabyForm(initial={'name':name, 'gender':gender, 'age':age, 'location':location, 'name_dropper':name_dropper, 'time_arrival':time_arrival, 'name_parents':name_parents, 'amount_paid':amount_paid, 'period_stay':period_stay}) # 'baby_number':baby_number})
    return render(request, 'baby_app/editbaby.html', {'form': form, 'baby_id':baby_id})    

#create view to delete baby 
def deletebaby(request, baby_id):
    Baby.objects.filter(id= baby_id).delete()
    redirect_url = reverse('baby')
    return HttpResponseRedirect(redirect_url)

#create view to Read baby 
def viewbaby(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    context = {'baby': baby}
    template = loader.get_template('baby_app/viewbaby.html')
    return HttpResponse(template.render(context))    

#create view for baby pick-up page   
def pickupbaby(request):
    babylist = Baby.objects.all()
    return render(request, 'baby_app/babypick.html', {'babylist': babylist})


def pickup(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name_dropper = form.cleaned_data['name_dropper']
            time_arrival = form.cleaned_data['time_arrival']
            baby_picked = form.cleaned_data['baby_picked']
            name_picker = form.cleaned_data['name_picker']
            comment = form.cleaned_data['comment']
            Baby.objects.create(name=name, name_dropper=name_dropper, time_arrival=time_arrival, baby_picked=baby_picked, name_picker=name_picker, comment=comment)
            return HttpResponseRedirect('pickupbaby')
    else:        
        form = PickupForm()
    babylist = Baby.objects.all()
    return render(request, 'baby_app/pickup.html', {'babylist': babylist})    


#create a view for the store page
def store_view(request):
    itemlist = Item.objects.all()
    return render(request, 'baby_app/store.html')


#create a view for the add item page
def add_Item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            Item.objects.create(name=name, quantity=quantity)
            return HttpResponseRedirect(reverse("store"))
    return render(request, 'baby_app/additem.html')


#create a view for the transactions page
def transaction_view(request):
    return render(request, 'baby_app/transactions.html')
