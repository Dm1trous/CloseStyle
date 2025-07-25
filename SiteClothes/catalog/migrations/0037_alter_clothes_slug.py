# Generated by Django 4.2.16 on 2024-10-27 10:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0036_clothes_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]
