# Generated by Django 3.2.9 on 2021-12-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211228_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото (Не обязательно)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото (Не обязательно)'),
        ),
    ]
