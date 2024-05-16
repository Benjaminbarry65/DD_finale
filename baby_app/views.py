from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.template import loader

# Create your views here.
#create views for baby page
def babyhome(request):
    #babyform = BabyForm()
    babylist = Baby.objects.all()
    return render(request, 'baby_app/baby.html', {'babylist': babylist})

#create view to add baby page
def addbaby(request):
    if request.method == 'POST':
        babyform = BabyForm(request.POST)
        print(request.POST)
        if babyform.is_valid():
            name = babyform.cleaned_data['name']
            gender = babyform.cleaned_data['gender']
            age = babyform.cleaned_data['age']
            location = babyform.cleaned_data['location']
            name_dropper = babyform.cleaned_data['name_dropper']
            time_arrival = babyform.cleaned_data['time_arrival']
            name_parents = babyform.cleaned_data['name_parents']
            amount_paid = babyform.cleaned_data['amount_paid']
            period_stay = babyform.cleaned_data['period_stay']
            #baby_number = babyform.cleaned_data['baby_number']
            Baby.objects.create(name=name, gender= gender, age=age, location=location, name_dropper=name_dropper, time_arrival=time_arrival, name_parents=name_parents, amount_paid=amount_paid, period_stay=period_stay) #baby_number=baby_number)
            return HttpResponseRedirect(reverse("baby"))
    else:
        babyform = BabyForm()
    babylist = Baby.objects.all()    
    return render(request, 'baby_app/addbaby.html', {'babylist': babylist, 'babyform':babyform})

#create view to edit baby page
def editbaby(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    if request.method == 'POST':
        babyform = BabyForm(request.POST)
        if babyform.is_valid():
            name = babyform.cleaned_data['name']
            gender = babyform.cleaned_data['gender'] 
            age = babyform.cleaned_data['age']
            location = babyform.cleaned_data['location']
            name_dropper = babyform.cleaned_data['name_dropper']
            time_arrival = babyform.cleaned_data['time_arrival']
            name_parents = babyform.cleaned_data['name_parents']
            amount_paid = babyform.cleaned_data['amount_paid']
            period_stay = babyform.cleaned_data['period_stay']
            #baby_number = babyform.cleaned_data['baby_number']

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
        babyform = BabyForm(initial={'name':baby.name, 'gender':baby.gender, 'age':baby.age, 'location':baby.location, 'name_dropper':baby.name_dropper, 'time_arrival':baby.time_arrival, 'name_parents':baby.name_parents, 'amount_paid':baby.amount_paid, 'period_stay':baby.period_stay}) # 'baby_number':baby_number})
    return render(request, 'baby_app/editbaby.html', {'babyform': babyform, 'baby_id':baby_id})    

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


def pickup(request):
    if request.method == 'POST':
        pickform = PickupForm(request.POST)
        if pickform.is_valid():
            baby_name = pickform.cleaned_data['baby_name']
            #baby_picked = pickform.cleaned_data['baby_picked']
            name_picker = pickform.cleaned_data['name_picker']
            comment = pickform.cleaned_data['comment']
            Pickup.objects.create(baby_name=baby_name, name_picker=name_picker, comment=comment)
            return HttpResponseRedirect('pickup')
    else:        
        pickform = PickupForm()
    pickuplist = Pickup.objects.all()
    return render(request, 'baby_app/pickup.html', {'pickuplist': pickuplist, 'pickform': pickform})    


#create a view for the store page
def store_view(request):
    itemlist = Item.objects.all()
    return render(request, 'baby_app/store.html', {'itemlist': itemlist})


#create a view for the add item page
def add_Item(request):
    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            item_name = itemform.cleaned_data['item_name']
            item_quantity = itemform.cleaned_data['item_quantity']
            Item.objects.create(item_name=item_name, item_quantity=item_quantity)
            return HttpResponseRedirect(reverse("store"))
    else:
        itemform = ItemForm()
    itemlist = Item.objects.all()        
    return render(request, 'baby_app/additem.html', {'itemlist': itemlist, 'itemform': itemform})

#create view to edit item
def edit_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            item_name = itemform.cleaned_data['item_name']
            item_quantity = itemform.cleaned_data['item_quantity']

          #updating fields in db  
            item.item_name = item_name
            item.item_quantity = item_quantity
            item.save()
            redirect_url = reverse('store')
            return HttpResponseRedirect(redirect_url)
    else:
        itemform = ItemForm(initial={'item_name':item.item_name, 'item_quantity':item.item_quantity})        
    return render(request, 'baby_app/edititem.html', {'itemform':itemform, 'item_id':item_id})    

#create view to delete item
def delete_item(request, item_id):
    Item.objects.filter(id= item_id).delete()
    redirect_url = reverse('store')
    return HttpResponseRedirect(redirect_url)    


#create a view for the transactions page
def transaction_view(request):
    translist = Baby.objects.values('name', 'amount_paid')
    doll_list = DollPay.objects.all()
    return render(request, 'baby_app/transactions.html', {'translist': translist, 'doll_list':doll_list})

#create a view for the doll payment page
def doll_pay(request):
    if request.method == 'POST':
        dollform = DollPayForm(request.POST)
        if dollform.is_valid():
            baby_name = dollform.cleaned_data['baby_name']
            doll_bought = dollform.cleaned_data['doll_bought']
            amount_paid = dollform.cleaned_data['amount_paid']
            quantity = dollform.cleaned_data['quantity']
            DollPay.objects.create(baby_name=baby_name, doll_bought=doll_bought, amount_paid=amount_paid, quantity=quantity)
            return HttpResponseRedirect(reverse("transactions"))
    else:
        dollform = DollPayForm()
    doll_list = DollPay.objects.all()
    return render(request, 'baby_app/dollpay.html', {'dollform': dollform}) 


#create a view for the duty page
def dutyadd(request):
    if request.method == 'POST':
        dutyform = DutyForm(request.POST)
        if dutyform.is_valid():
            name_sitter = dutyform.cleaned_data['name_sitter']
            name_baby = dutyform.cleaned_data['name_baby']
            #duty_date = dutyform.cleaned_data['duty_date']
            Duty.objects.create(name_sitter=name_sitter, name_baby=name_baby) #, duty_date=duty_date)
            return HttpResponseRedirect(reverse('duty'))
    else:
        dutyform = DutyForm()
    dutylist = Duty.objects.all()            
    return render(request, 'baby_app/duty.html', {'dutylist': dutylist, 'dutyform': dutyform})      
