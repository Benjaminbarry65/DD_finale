from django.db import models
from daystar_app.models import Sitter

# Create your models here.
#name of baby
#gender
#age
#location
#name of dropper
#time of arrival
#parents name
#Fee paid(UGX)
#period of stay
#baby number

class Baby(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    name_dropper = models.CharField(max_length=100)
    time_arrival = models.TimeField()
    name_parents = models.CharField(max_length=100)
    amount_paid = models.IntegerField()
    period_stay = models.CharField(max_length=50)
    #baby_number = models.IntegerField()
    
    def __str__(self):
        return self.name

class Pickup(models.Model):
    baby_name = models.ForeignKey(Baby, on_delete=models.CASCADE)
    baby_picked = models.DateTimeField(auto_now_add=True)  
    name_picker = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.baby_name
    


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_quantity = models.IntegerField()

    def __str__(self):
        return self.item_name


# class Transaction(models.Model):
#     baby_name = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='baby_transactions')
#     fee_paid = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='fee_transactions')

#     def __str__(self):
#         return f"Transaction - {self.name, self.amount_paid}"


class DollPay(models.Model):
    baby_name = models.ForeignKey(Baby, on_delete=models.CASCADE)
    doll_bought = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.baby_name


class Duty(models.Model):
    name_sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    name_baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    duty_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Duty - {self.name, self.name}"        
            

        