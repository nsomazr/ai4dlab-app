from django import forms
from django.utils import timezone
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class WorkshopForm(forms.Form):
    workshop_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Workshop Name'})))
    workshop_url  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'website', 'placeholder':'Website URL'})))
    description  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': False, 'cols': 100, 'rows': 10, 'id':'Description'}))
   


    