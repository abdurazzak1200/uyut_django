from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    img = models.ImageField(upload_to='category/', default='products/no.jpeg', verbose_name='Фото (Не обязательно)')

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='название подкотегории')
    img = models.ImageField(upload_to='category/', default='products/no.jpeg', verbose_name='Фото (Не обязательно)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = "Подкатегорию"
        verbose_name_plural = "Подкатегории"
    def __str__(self):
        return self.name

class Size_Product(models.Model):
    name = models.CharField(max_length=10, verbose_name='Размер')

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"
    def __str__(self):
        return self.name

class Carousel(models.Model):
    img = models.ImageField(upload_to='photo/')
    price = models.CharField(max_length=6, verbose_name='Цена')
    year = models.CharField(max_length=4, verbose_name='Год')
    name = models.CharField(max_length=100, verbose_name='Наименование коллекции')

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.CharField(max_length=6, verbose_name='Цена')
    category = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        null=True,
    )
    size = models.ForeignKey(
        Size_Product,
        on_delete=models.PROTECT,
        verbose_name="Размер (Не обязательно)",
        null=True,
        blank=True
    )
    img = models.ImageField(upload_to='products/', verbose_name='Фото (Необязательно)', default='products/no.jpeg')
    img2 = models.ImageField(upload_to='products/', verbose_name='Фото (Не обязательно)', null=True,blank=True)
    img3 = models.ImageField(upload_to='products/', verbose_name='Фото (Не обязательно)', null=True,blank=True)
    img4 = models.ImageField(upload_to='products/', verbose_name='Фото (Не обязательно)', null=True,blank=True)
    img5 = models.ImageField(upload_to='products/', verbose_name='Фото (Не обязательно)', null=True,blank=True)
    descript = models.TextField(verbose_name='Описание (Не обязательно)', default='Описание отсутствует')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class Adress(models.Model):
    adress = models.CharField(max_length=100, verbose_name='Адресс')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона (Не обязательно)', null=True, blank=True)
    tg = models.CharField(max_length=200, verbose_name='Телеграм (Не обязательно)', null=True, blank=True)


    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.adress


class Message(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    message = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"

    def __str__(self):
        return self.message
