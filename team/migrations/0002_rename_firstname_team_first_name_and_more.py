# Generated by Django 4.1.6 on 2023-02-08 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='team_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='linkedin',
            new_name='linkedin_url',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='twitter',
            new_name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='team',
            name='affiliate',
        ),
        migrations.AddField(
            model_name='team',
            name='affiliation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]