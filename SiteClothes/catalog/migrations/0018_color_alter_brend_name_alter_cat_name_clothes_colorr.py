# Generated by Django 4.2.16 on 2024-10-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_size_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвет',
            },
        ),
        migrations.AlterField(
            model_name='brend',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='colorr',
            field=models.ManyToManyField(to='catalog.color', verbose_name='Цвет'),
        ),
    ]