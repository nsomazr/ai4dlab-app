# Generated by Django 4.1.6 on 2023-05-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_remove_publication_banner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='file',
            field=models.FileField(blank=True, max_length=500, upload_to='publication'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]