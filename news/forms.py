from django import forms
from django.utils import timezone
from .models import News
from tinymce.widgets import TinyMCE
from ckeditor.fields import RichTextField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

ta =(
    (0, "General"),
    (1, "Health Care"),
    (2, "Agriculture and Environmental Conversation"),
    (3, "Infrastructure and Data Ecosystem"),
    (4, "Digital Economy and Small Scale Industry"),
)
class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
class NewsForm(forms.ModelForm):
    thematic_area = forms.ChoiceField(choices=ta,widget=(forms.Select(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    title  = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    thumbnail = forms.ImageField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
    header_image = forms.ImageField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose image'})))
    description = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id': 'description','placeholder': 'Description'})))
    file = forms.FileField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose File'})))
    # body  = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10, 'id':'body'}))
    # body = RichTextField()
    body = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': False, 'cols': 100, 'rows': 10, 'id':'body'}))
    
    class Meta:
        model = News
        fields = ('thematic_area', 'title', 'description', 'thumbnail', 'header_image', 'body')

  
  


    