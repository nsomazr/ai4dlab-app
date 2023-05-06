from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
import os
from django_resized import ResizedImageField
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    header_image = ResizedImageField(size=[1400, 600],scale=0.5, quality=100, crop=['middle', 'center'], null=False, blank=True, force_format='PNG',upload_to=os.path.join(BASE_DIR,'publication'))
    file = models.FileField(max_length=500, blank=True,upload_to=os.path.join(BASE_DIR,'publication'))
    description = models.TextField(max_length=500)
    body = RichTextUploadingField(blank=True,null=True)
    thematic_area = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    publish = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=False, unique=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

        

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("publication_detail", kwargs={"slug": self.slug}) 
