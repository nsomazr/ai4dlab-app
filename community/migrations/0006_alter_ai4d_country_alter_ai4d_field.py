# Generated by Django 4.1.6 on 2023-03-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_rename_programme_ai4d_affiliation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai4d',
            name='country',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ai4d',
            name='field',
            field=models.CharField(max_length=200),
        ),
    ]
