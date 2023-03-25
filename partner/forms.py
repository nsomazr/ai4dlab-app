from django import forms
from django.utils import timezone
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class PartnerForm(forms.Form):
    partner_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Partner Name'})))
    website_url  = forms.URLField(max_length=100, widget=(forms.URLInput(attrs={'class': 'form-control', 'id':'website', 'placeholder':'Website URL'})))
    description = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': False, 'cols': 100, 'rows': 10, 'id':'body'}))
    logo = forms.ImageField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
   


    