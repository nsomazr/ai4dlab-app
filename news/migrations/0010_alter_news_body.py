# Generated by Django 4.1.6 on 2023-03-11 11:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_news_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
