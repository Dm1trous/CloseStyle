# Generated by Django 4.2.16 on 2024-10-26 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_remove_profile_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]