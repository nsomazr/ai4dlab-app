# Generated by Django 4.1.6 on 2023-05-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0005_alter_call_file_alter_call_slug_alter_call_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
