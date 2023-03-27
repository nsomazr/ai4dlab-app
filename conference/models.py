from django.db import models
from django.utils import timezone
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class CallPaperAAIAC(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title= models.CharField(default=None, max_length=100)
    bio = RichTextUploadingField(blank=True,null=True)
    linkedin_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    affiliation = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=False)
    status = models.IntegerField(default=0)
    photo  = models.ImageField(max_length=255, upload_to=os.path.join(BASE_DIR,'team'), default=None, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class RegistrationAAIAC(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title= models.CharField(default=None, max_length=100)
    bio = RichTextUploadingField(blank=True,null=True)
    linkedin_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    affiliation = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=False)
    status = models.IntegerField(default=0)
    photo  = models.ImageField(max_length=255, upload_to=os.path.join(BASE_DIR,'team'), default=None, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    def __str__(self):
        return self.username

class Conference(models.Model):
    pass