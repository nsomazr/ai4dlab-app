from django import forms
from django.utils import timezone

class WorkshopForm(forms.Form):
    partner_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Partner Name'})))
    website_url  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'website', 'placeholder':'Website URL'})))
    logo = forms.ImageField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
   


    