from django import forms
from django.utils import timezone
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget

ta =(
    (0, "General"),
    (1, "Health Care"),
    (2, "Agriculture and Environmental Conversation"),
    (3, "Infrastructure and Data Ecosystem"),
    (4, "Digital Economy and Small Scale Industry"),
)

class BlogForm(forms.ModelForm):
    title  = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    thematic_area = forms.ChoiceField(choices=ta, widget=(forms.Select(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    thumbnail = forms.ImageField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
    description  = forms.CharField(max_length=5000, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'bio', 'placeholder':'Description'})))
    body = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': False, 'cols': 100, 'rows': 10, 'id':'body'}))
    header_image = forms.ImageField(required=False, max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image','required':'false'})))
    file = forms.FileField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose File'})))
    # author  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'publisher-name', 'placeholder':'Full Name'})))
    
    class Meta:
        model = Blog
        fields = ['header_image']


    