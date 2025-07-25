# Generated by Django 5.2.1 on 2025-06-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0100_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(verbose_name='Итоговая стоимость'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(verbose_name='Цена за единицу'),
        ),
    ]
