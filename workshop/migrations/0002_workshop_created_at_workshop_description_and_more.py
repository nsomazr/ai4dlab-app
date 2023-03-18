# Generated by Django 4.1.6 on 2023-03-18 06:30

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='workshop',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='published',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workshop',
            name='publisher',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workshop',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='workshop',
            name='workshop_name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='workshop_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workshop',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
