# Generated by Django 4.2.16 on 2024-10-25 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_clothes_options_clothes_brendd_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name': 'Пол', 'verbose_name_plural': 'Для кого'},
        ),
        migrations.AlterField(
            model_name='clothes',
            name='brendd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.brend', verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='catt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.cat', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Для кого'),
        ),
    ]
