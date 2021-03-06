# Generated by Django 3.2.9 on 2021-12-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20211228_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=100, verbose_name='Адресс')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона (Не обязательно)')),
                ('tg', models.CharField(blank=True, max_length=200, null=True, verbose_name='Телеграм (Не обязательно)')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]
