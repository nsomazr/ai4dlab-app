# Generated by Django 4.1.6 on 2023-12-25 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_userprofile_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='updated_at',
        ),
    ]