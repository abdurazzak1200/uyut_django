# Generated by Django 3.2.9 on 2021-12-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_size_size_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(null=True, upload_to='products/', verbose_name='Фото (Не обязательно)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(null=True, upload_to='products/', verbose_name='Фото (Не обязательно)'),
        ),
    ]
