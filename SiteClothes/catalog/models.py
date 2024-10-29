from django.db import models
from django.contrib.auth.models import User


class clothes(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    summ = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Стоимость")
    catt = models.ForeignKey('cat', on_delete=models.CASCADE, verbose_name="Категория")
    genderr = models.ForeignKey('gender', on_delete=models.CASCADE, verbose_name="Для")
    sizee = models.ManyToManyField('size', verbose_name="Размер", related_name='size')
    materiall = models.ManyToManyField('material', verbose_name="Материал")
    colorr = models.ForeignKey('color', on_delete=models.CASCADE, verbose_name="Цвет")
    brendd = models.ForeignKey('brend', on_delete=models.CASCADE, verbose_name="Бренд")
    statuss = models.BooleanField(default=True, verbose_name="В наличии")
    imgg = models.ImageField(verbose_name="Фото", upload_to='image/')
    dates = models.DateTimeField(auto_now=True)


    def display_size(self):
        return ', '.join([sizee.name for sizee in self.sizee.all()])
    display_size.short_description = 'Размер'

    def display_material(self):
        return ', '.join([materiall.name for materiall in self.materiall.all()])
    display_material.short_description = 'материал'

    class Meta:
        verbose_name = 'Одежду'
        verbose_name_plural = 'Вся одежда'

    def __str__(self):
        return self.title

class brend(models.Model):
    name = models.CharField(max_length=50, verbose_name="Бренд")
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Список брендов'
    def __str__(self):
        return self.name

class gender(models.Model):
    name = models.CharField(max_length=20, verbose_name="Для кого")
    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Для кого'
    def __str__(self):
        return self.name

class size(models.Model):
    name = models.CharField(max_length=20, verbose_name="Введите размер")
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Все размеры'
    def __str__(self):
        return self.name

class cat(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория")
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

class color(models.Model):
    name = models.CharField(max_length=50, verbose_name="Цвет")
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'
    def __str__(self):
        return self.name

class material(models.Model):
    name = models.CharField(max_length=50, verbose_name="Материал")
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материал'
    def __str__(self):
        return self.name

class newss(models.Model):
    name = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(max_length=5000, verbose_name="Текст статьи")
    img = models.ImageField(verbose_name="Фото", upload_to='image/', help_text="Рекомендуется изображение формата 1x1")
    dates = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статья'
    def __str__(self):
        return self.name

#
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='products/')
#
#     def __str__(self):
#         return self.name

class CartItem(models.Model):
    product = models.ForeignKey(clothes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'