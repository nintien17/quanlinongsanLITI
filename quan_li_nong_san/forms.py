from django import forms

class fruitForm(forms.Form):
    id= forms.IntegerField()
    name= forms.CharField(max_length=100)
    xuatxu= forms.CharField(max_length=100)
    price= forms.FloatField()