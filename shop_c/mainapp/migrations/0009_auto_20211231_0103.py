# Generated by Django 3.2.5 on 2021-12-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20211113_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_l',
            field=models.ImageField(default=1, help_text='Загружайте изображения стороны данного товара', upload_to='', verbose_name='Боковые изображения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_r',
            field=models.ImageField(default=1, help_text='Загружайте изображения стороны данного товара', upload_to='', verbose_name='Боковые изображения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Старая Цена (зачеркнутая цена)'),
            preserve_default=False,
        ),
    ]
