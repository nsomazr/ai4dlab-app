# Generated by Django 4.1.6 on 2023-02-13 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab', '0002_rename_name_colab_partner_name_remove_colab_about_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colab',
            old_name='partner_name',
            new_name='colab_name',
        ),
    ]