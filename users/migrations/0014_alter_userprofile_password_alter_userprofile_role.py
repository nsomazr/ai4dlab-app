# Generated by Django 4.1.6 on 2024-01-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('pi', 'Principal Investigator'), ('co_pi', 'Co-Principal Investigator'), ('ltc', 'Lab Training Coordinator'), ('lo', 'Laison Officer'), ('coordinator', 'Coordinator'), ('asst_coordinator', 'Assistant Coordinator'), ('researcher', 'Researcher'), ('asst_researcher', 'Assistant Researcher'), ('innovator', 'Innovator'), ('student', 'Student')], max_length=20),
        ),
    ]