from django import forms
from django.utils import timezone
from .models import Call
from ckeditor_uploader.widgets import CKEditorUploadingWidget

ta =(
    (0, "General"),
    (1, "Health Care"),
    (2, "Agriculture and Environmental Conversation"),
    (3, "Infrastructure and Data Ecosystem"),
    (4, "Digital Economy and Small Scale Industry"),
)

class CallForm(forms.ModelForm):
    title  = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    thematic_area = forms.ChoiceField(choices=ta, widget=(forms.Select(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    file = forms.FileField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose File'})))
    thumbnail = forms.ImageField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
    header_image = forms.ImageField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
    description  = forms.CharField(max_length=5000, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'bio', 'placeholder':'Description'})))
    body = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': False, 'cols': 100, 'rows': 10, 'id':'body'}))
    
    class Meta:
        model = Call
        fields = ['file']


    