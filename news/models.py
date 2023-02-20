from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField
# Create your models here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    banner = ResizedImageField(size=[1080, 1080],scale=0.5, quality=100, crop=['middle', 'center'], null=False, blank=True, force_format='PNG',upload_to=os.path.join(BASE_DIR,'news'))
    body = models.TextField()
    content_photo_one = ResizedImageField(size=[600, 400],scale=0.5,crop=['middle', 'center'], quality=100, null=False, blank=True, force_format='PNG',upload_to=os.path.join(BASE_DIR,'news'))
    content_photo_two = ResizedImageField(size=[600, 400],scale=0.5,crop=['middle', 'center'], quality=100, null=False, blank=True, force_format='PNG',upload_to=os.path.join(BASE_DIR,'news'))
    content_photo_three =ResizedImageField(size=[600, 400],scale=0.5,crop=['middle', 'center'], quality=100, null=False, blank=True, force_format='PNG',upload_to=os.path.join(BASE_DIR,'news'))
    status = models.IntegerField(default=0)
    publish = models.IntegerField(default=0)
    reject = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    publisher = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

        

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug}) 
