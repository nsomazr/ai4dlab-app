# Generated by Django 4.1.6 on 2023-03-25 14:01

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab', '0004_alter_colab_website_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='colab',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]