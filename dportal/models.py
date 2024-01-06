from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class DPortal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    file = models.FileField(max_length=500, blank=True,upload_to=os.path.join(BASE_DIR,'dportal'))
    description = models.TextField()
    body = RichTextUploadingField(blank=True,null=True)
    thematic_area = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    publish = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=False, unique=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

        

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("data_detail", kwargs={"slug": self.slug}) 

class PatientData(models.Model):
    patient_id = models.CharField(max_length=500)
    age = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    facility = models.CharField(max_length=500)
    main_complaint = RichTextUploadingField()
    history_of_present_illness = RichTextUploadingField()
    review_of_other_systems = RichTextUploadingField()
    past_medical_history = RichTextUploadingField()
    gynaecological_history = RichTextUploadingField()
    family_social_history = RichTextUploadingField()
    dietary_history = RichTextUploadingField()
    general_examination = RichTextUploadingField()
    local_examination = RichTextUploadingField()
    systemic_examination = RichTextUploadingField()
    provisional_diagnosis = RichTextUploadingField()
    differential_diagnosis = RichTextUploadingField()
    final_diagnosis = RichTextUploadingField()
    radiological = RichTextUploadingField()
    laboratory = RichTextUploadingField()
    doctors_remarks = RichTextUploadingField()
    medicines = RichTextUploadingField()
    treatment_regime = RichTextUploadingField()
    recommendation = RichTextUploadingField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user_id = models.IntegerField(default=0)
    def __str__(self):
        return self.patient_id  # Display the patient's ID in the admin panel

