from django.db import models
from django.utils import timezone
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    title= models.CharField(default=None, max_length=100)
    bio = models.TextField()
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=100)
    affiliate = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    status = models.IntegerField(default=0)
    photo  = models.ImageField(max_length=255, upload_to=os.path.join(BASE_DIR,'media/team'), default=None, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
