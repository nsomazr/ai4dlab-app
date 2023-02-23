from django import forms
from django.utils import timezone
from .models import News

class NewsForm(forms.ModelForm):
    title  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    banner = forms.ImageField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
    body  = forms.CharField(max_length=5000, widget=(forms.Textarea(attrs={'class': 'form-control', 'id':'bio', 'placeholder':'Body'})))
    content_photo_one = forms.ImageField(required=False, max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image','required':'false'})))
    content_photo_two = forms.ImageField(required=False, max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image', 'required':'false'})))
    content_photo_three = forms.ImageField(required=False, max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image', 'required':'false'})))
    publisher  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'publisher-name', 'placeholder':'Full Name'})))
    
    class Meta:
        model = News
        fields = ['content_photo_one','content_photo_two','content_photo_three']


    