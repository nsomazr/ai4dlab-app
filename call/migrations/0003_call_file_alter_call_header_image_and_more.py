# Generated by Django 4.1.6 on 2023-03-16 14:29

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0002_rename_publisher_call_author_remove_call_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='file',
            field=models.FileField(blank=True, upload_to='call'),
        ),
        migrations.AlterField(
            model_name='call',
            name='header_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, quality=100, scale=0.5, size=[1400, 600], upload_to='call'),
        ),
        migrations.AlterField(
            model_name='call',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, quality=100, scale=0.5, size=[600, 400], upload_to='call'),
        ),
    ]
