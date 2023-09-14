from django import forms
from django.utils import timezone
from .models import DPortal
from ckeditor_uploader.widgets import CKEditorUploadingWidget

ta =(
    (0, "General"),
    (1, "Health Care"),
    (2, "Agriculture and Environmental Conversation"),
    (3, "Infrastructure and Data Ecosystem"),
    (4, "Digital Economy and Small Scale Industry"),
)

class DataForm(forms.ModelForm):
    name  = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    thematic_area = forms.ChoiceField(choices=ta, widget=(forms.Select(attrs={'class': 'form-control', 'id':'partner-name', 'placeholder':'Title'})))
    file = forms.FileField(max_length=500, widget=(forms.FileInput(attrs={'class': 'form-control ','id': 'photo','placeholder': 'Choose File'})))
    description  = forms.CharField(max_length=5000, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'bio', 'placeholder':'Description'})))
    body = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': False, 'cols': 100, 'rows': 10, 'id':'body'}))
    
    class Meta:
        model = DPortal
        fields = ['file']


class PatientDataForm(forms.Form):
    patient_id  = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'first-name', 'placeholder':'Patient ID'})))
    age  = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':';last-name', 'placeholder':'Age'})))
    country  = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'title', 'placeholder':'Country'})))
    district = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'affiliation', 'placeholder':'District'})))
    region = forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'affiliation', 'placeholder':'region'})))
    main_complaint  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'main_complaint'}))
    history_of_present_illness  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'history_of_present_illness'}))
    review_of_other_systems  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'review_of_other_systems'}))
    past_medical_history  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'past_medical_history'}))
    gynaecological_history = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'gynaecological_history'}))
    family_social_history  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'family_social_history'}))
    dietary_history  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'dietary_history'}))
    general_examination  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'general_examination'}))
    local_examination  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'local_examination'}))
    systemic_examination = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'systemic_examination'}))
    provisional_diagnosis  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'provisional_diagnosis'}))
    differential_diagnosis  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'differential_diagnosis'}))
    final_diagnosis  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'final_diagnosis'}))
    radiological = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'radiological'}))
    laboratory = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'laboratory'}))
    doctors_remarks  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'doctors_remarks'}))
    medicines  = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'medicines'}))
    treatment_regime = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'treatment_regime'}))
    recommendation = forms.CharField(widget=CKEditorUploadingWidget(attrs={'required': True, 'cols': 100, 'rows': 10, 'id':'recommendation'}))
    