from django import forms
from django.utils import timezone
from .models import Blog

class BlogForm(forms.ModelForm):
    title  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    thumbnail = forms.ImageField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
    description  = forms.CharField(max_length=5000, widget=(forms.Textarea(attrs={'class': 'form-control', 'id':'bio', 'placeholder':'Description'})))
    body  = forms.CharField(max_length=5000, widget=(forms.Textarea(attrs={'class': 'form-control', 'id':'bio', 'placeholder':'Body'})))
    header_image = forms.ImageField(required=False, max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image','required':'false'})))
    author  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'publisher-name', 'placeholder':'Full Name'})))
    
    class Meta:
        model = Blog
        fields = ['header_image']


    