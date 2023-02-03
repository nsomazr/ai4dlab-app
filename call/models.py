from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class Call(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=100)
    banner = models.ImageField(max_length=100, blank=True,upload_to=os.path.join(BASE_DIR,'media/call'))
    document = models.ImageField(max_length=100, blank=True,upload_to=os.path.join(BASE_DIR,'media/call'))
    description = models.TextField()
    body = models.TextField()
    status = models.IntegerField(default=0)
    slug = models.SlugField(null=False, unique=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

        

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("call_detail", kwargs={"slug": self.slug}) 
