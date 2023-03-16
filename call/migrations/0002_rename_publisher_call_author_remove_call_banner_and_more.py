# Generated by Django 4.1.6 on 2023-03-16 13:53

import ckeditor_uploader.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='call',
            old_name='publisher',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='call',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='call',
            name='document',
        ),
        migrations.RemoveField(
            model_name='call',
            name='headline',
        ),
        migrations.AddField(
            model_name='call',
            name='header_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, quality=100, scale=0.5, size=[1400, 600], upload_to='blog'),
        ),
        migrations.AddField(
            model_name='call',
            name='publish',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='call',
            name='thematic_area',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='call',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, quality=100, scale=0.5, size=[600, 400], upload_to='blog'),
        ),
        migrations.AddField(
            model_name='call',
            name='title',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='call',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='call',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
