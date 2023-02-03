from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class Jupyinter(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(max_length = 10, default=0)
    active = models.IntegerField(default=0)
    uploads = models.ImageField(max_length=200, blank=True,upload_to=os.path.join(BASE_DIR,'media/jupyinter'))
    slug = models.SlugField(null=False, unique=True)
    status = models.IntegerField(default=0)
    opened_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

        

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jupyinter_detail", kwargs={"slug": self.slug}) 
