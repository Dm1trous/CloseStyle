# Generated by Django 4.2.16 on 2024-10-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_material_remove_clothes_colorr_clothes_materiall_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='imgg',
            field=models.ImageField(default=1, upload_to='image/', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
