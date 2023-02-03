# Generated by Django 4.1.4 on 2023-01-21 10:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('banner', models.ImageField(blank=True, upload_to='media/event')),
                ('content_photo_one', models.ImageField(blank=True, upload_to='media/event')),
                ('content_photo_two', models.ImageField(blank=True, upload_to='media/event')),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
