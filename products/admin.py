from django.contrib import admin
from .models import Carousel, Category, Size_Product, Product, Adress, SubCategory

# Register your models here.

admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(Size_Product)
admin.site.register(Product)
admin.site.register(Adress)
admin.site.register(SubCategory)