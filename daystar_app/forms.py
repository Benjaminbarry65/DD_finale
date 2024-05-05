from django import forms

class SitterForm(forms.Form):
    name = forms.CharField(max_length=100)
    gender = forms.CharField()
    #date_admitted = forms.DateField()
    contact = forms.CharField(max_length=13)
    #duty = forms.BooleanField(required=False)