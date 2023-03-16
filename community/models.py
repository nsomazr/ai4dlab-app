from django.db import models
from django.utils import timezone
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class UDOMAI(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    college= models.IntegerField(default=0)
    programme = models.CharField(max_length=200)
    yos =models.IntegerField(default=0)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=False)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)