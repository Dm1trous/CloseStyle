# Generated by Django 4.2.16 on 2024-10-25 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_clothes_sizee'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='statuss',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Статус'),
            preserve_default=False,
        ),
    ]