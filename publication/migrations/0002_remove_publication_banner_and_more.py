# Generated by Django 4.1.6 on 2023-03-17 20:57

import ckeditor_uploader.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='document',
        ),
        migrations.AddField(
            model_name='publication',
            name='file',
            field=models.FileField(blank=True, upload_to='publication'),
        ),
        migrations.AddField(
            model_name='publication',
            name='header_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, quality=100, scale=0.5, size=[1400, 600], upload_to='publication'),
        ),
        migrations.AddField(
            model_name='publication',
            name='publish',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='publication',
            name='thematic_area',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='publication',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]