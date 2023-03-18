# Generated by Django 4.1.6 on 2023-03-18 05:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_alter_news_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, quality=100, scale=0.5, size=[1080, 1080], upload_to='news'),
        ),
    ]
