# Generated by Django 4.2.16 on 2024-10-27 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0040_service_delete_artists'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
    ]