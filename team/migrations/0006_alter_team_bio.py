# Generated by Django 4.1.6 on 2023-03-25 13:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_alter_team_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
