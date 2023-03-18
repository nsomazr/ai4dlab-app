from django.db import models
from django.utils import timezone
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))
class Sponsor(models.Model):
    id = models.AutoField(primary_key=True)
    sponsor_name = models.CharField(max_length=100)
    website_url = models.URLField(max_length=100)
    logo = models.ImageField(max_length=100, blank=True,upload_to=os.path.join(BASE_DIR,'sponsor'))
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sponsor_name