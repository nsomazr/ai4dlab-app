# Generated by Django 4.1.6 on 2023-02-20 20:07

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_reject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='banner',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1080, 1080], upload_to='news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_photo_one',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[600, 400], upload_to='news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_photo_three',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[600, 400], upload_to='news'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='content_photo_two',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[600, 400], upload_to='news'),
            preserve_default=False,
        ),
    ]
