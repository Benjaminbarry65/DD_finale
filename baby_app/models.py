from django.db import models

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
    time_arrival = models.DateTimeField(auto_now_add=True)
    name_parents = models.CharField(max_length=100)
    amount_paid = models.FloatField()
    period_stay = models.CharField(max_length=50)
    #baby_number = models.IntegerField()
    
    def __str__(self):
        return self.name

class Pickup(models.Model):
    baby_info = models.ForeignKey(Baby, on_delete=models.CASCADE)
    baby_picked = models.DateTimeField(auto_now_add=True)  
    name_picker = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)

    @property
    def name(self):
        return self.baby_info.name 

    @property
    def name_dropper(self):
        return self.baby_info.name_dropper

    @property
    def time_arrival(self):
        return self.baby_info.time_arrival


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_quantity = models.IntegerField()

    def __str__(self):
        return self.item_name

        