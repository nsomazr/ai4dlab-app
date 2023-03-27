from django import forms
from django.utils import timezone
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CallPaperFormAAIAC(forms.Form):
    first_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'first-name', 'placeholder':'First Name'})))
    last_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':';last-name', 'placeholder':'Last Name'})))
    title  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'title', 'placeholder':'title'})))
    affiliation  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'affiliation', 'placeholder':'Affiliation'})))
    bio = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': False, 'cols': 100, 'rows': 10, 'id':'body'}))
    linkedin_url  = forms.URLField(max_length=100, widget=(forms.URLInput(attrs={'class': 'form-control', 'id':'linkedin', 'placeholder':'Linkedin URL'})))
    twitter_url  = forms.URLField(max_length=100, widget=(forms.URLInput(attrs={'class': 'form-control', 'id':'twitter', 'placeholder':'Twitter URL'})))
    phone  = forms.IntegerField(widget=(forms.NumberInput(attrs={'class': 'form-control', 'id':'phone-number', 'placeholder':'Phone Number'})))
    email  = forms.EmailField(max_length=100, widget=(forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'placeholder':'Email Address'})))
    photo = forms.ImageField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))


class RegistrationAAIAC(forms.Form):
    first_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'first-name', 'placeholder':'First Name'})))
    last_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':';last-name', 'placeholder':'Last Name'})))
    title  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'title', 'placeholder':'title'})))
    affiliation  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'affiliation', 'placeholder':'Affiliation'})))
    bio = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': False, 'cols': 100, 'rows': 10, 'id':'body'}))
    linkedin_url  = forms.URLField(max_length=100, widget=(forms.URLInput(attrs={'class': 'form-control', 'id':'linkedin', 'placeholder':'Linkedin URL'})))
    twitter_url  = forms.URLField(max_length=100, widget=(forms.URLInput(attrs={'class': 'form-control', 'id':'twitter', 'placeholder':'Twitter URL'})))
    phone  = forms.IntegerField(widget=(forms.NumberInput(attrs={'class': 'form-control', 'id':'phone-number', 'placeholder':'Phone Number'})))
    email  = forms.EmailField(max_length=100, widget=(forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'placeholder':'Email Address'})))
    photo = forms.ImageField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))

class ConferenceForm(forms.Form):
    partner_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Partner Name'})))
    website_url  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'website', 'placeholder':'Website URL'})))
    logo = forms.ImageField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
   


    