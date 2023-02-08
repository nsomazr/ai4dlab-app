from django import forms
from django.utils import timezone

class TeamForm(forms.Form):
    first_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'first-name', 'placeholder':'First Name'})))
    last_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':';last-name', 'placeholder':'Last Name'})))
    title  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'title', 'placeholder':'title'})))
    affiliation  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'affiliation', 'placeholder':'Affiliation'})))
    bio  = forms.CharField(max_length=5000, widget=(forms.Textarea(attrs={'class': 'form-control', 'id':'bio', 'placeholder':'Bio'})))
    linkedin_url  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'linkedin', 'placeholder':'Linkedin URL'})))
    twitter_url  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'twitter', 'placeholder':'Twitter URL'})))
    phone  = forms.IntegerField(widget=(forms.NumberInput(attrs={'class': 'form-control', 'id':'phone-number', 'placeholder':'Phone Number'})))
    email  = forms.EmailField(max_length=100, widget=(forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'placeholder':'Email Address'})))
    photo = forms.ImageField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
   


    