# Generated by Django 3.2.16 on 2023-01-10 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0002_auto_20230109_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='our_volunteers',
            old_name='volunteer_reason_to_be_a_volunter',
            new_name='volunteer_reason_to_be_a_volunteer',
        ),
    ]
