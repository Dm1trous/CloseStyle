# Generated by Django 4.2.16 on 2024-10-27 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0037_alter_clothes_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes',
            name='slug',
        ),
    ]