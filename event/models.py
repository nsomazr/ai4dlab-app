from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    banner = models.ImageField(max_length=100, blank=True,upload_to=os.path.join(BASE_DIR,'media/event'))
    content_photo_one = models.ImageField(max_length=100, blank=True,upload_to=os.path.join(BASE_DIR,'media/event'))
    content_photo_two = models.ImageField(max_length=100, blank=True,upload_to=os.path.join(BASE_DIR,'media/event'))
    description = models.TextField()
    body = models.TextField()
    status = models.IntegerField(default=0)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug}) 
