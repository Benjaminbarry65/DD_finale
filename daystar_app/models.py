from django.db import models

# Create your models here.
#Name
#Gender
#Date_admitted
#Contact
#duty

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=25)
    #date_admitted = models.DateField()
    contact = models.CharField(max_length=25)
    #duty = models.BooleanField(default=False)