# Generated by Django 3.2.9 on 2021-12-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20211229_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(default='products/no.jpeg', upload_to='category/', verbose_name='Фото (Необязательно)'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='img',
            field=models.ImageField(default='products/no.jpeg', upload_to='category/', verbose_name='Фото (Необязательно)'),
        ),
    ]