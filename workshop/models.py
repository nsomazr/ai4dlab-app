from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))
class Workshop(models.Model):
    id = models.AutoField(primary_key=True)
    workshop_name = models.CharField(max_length=200)
    workshop_url = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=True,null=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    publish = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.workshop_name