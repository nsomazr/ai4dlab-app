# Generated by Django 4.1.6 on 2023-03-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_alter_news_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content_photo_one',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_photo_three',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_photo_two',
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
