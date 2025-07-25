# Generated by Django 4.2.16 on 2024-10-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0045_alter_newss_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='newss',
            name='dates',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='newss',
            name='img',
            field=models.ImageField(help_text='Рекомендуется изображение формата 1x1', upload_to='image/', verbose_name='Фото'),
        ),
    ]
