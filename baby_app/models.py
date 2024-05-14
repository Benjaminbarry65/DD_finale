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
    #baby_name = models.ForeignKey(Baby, on_delete=models.CASCADE, null=False, blank=False, default=0)
    #baby_dropper = models.ForeignKey(Baby, on_delete=models.CASCADE)
    #baby_arrival = models.ForeignKey(Baby, on_delete=models.CASCADE)
    baby_picked = models.DateTimeField(auto_now_add=True)  
    name_picker = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.name 

        