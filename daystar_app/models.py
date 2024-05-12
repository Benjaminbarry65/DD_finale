from django.db import models

# Create your models here.
#Name
#location
#DOB
#Gender
#next of kin
#NIN
#recommenders name
#religion
#level of education
#sitter number
#Contact
#duty

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=25)
    next_kin = models.CharField(max_length=100)
    nin = models.CharField(max_length=100)
    recomm_name = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)
    level_education = models.CharField(max_length=200)
    contact = models.IntegerField()
    #duty = models.BooleanField(default=False)

    def __str__(self):
        return self.name