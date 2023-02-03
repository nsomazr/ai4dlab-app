from django.db import models
from django.utils import timezone
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))
class Conference(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    banner = models.ImageField(max_length=100, blank=True,upload_to=os.path.join(BASE_DIR,'media/conference'))
    document = models.FileField(max_length=100, upload_to=os.path.join(BASE_DIR,'media/conference'))
    description = models.TextField()
    body = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
