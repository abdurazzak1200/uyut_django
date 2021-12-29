from django.shortcuts import render
from .models import Carousel, Product, Adress, Category, SubCategory
# Create your views here.

def index(request):
    carousels = Carousel.objects.all()
    products = Product.objects.all()
    context = {'carousels': carousels, 'products':products}
    return render(request,'index.html', context)
def product_deteil(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product":product,
    }
    return render(request, "product_deteil.html", context=context)
def contact(request):
    adresses = Adress.objects.all()
    context = {'adresses': adresses}
    return render(request, 'contact.html', context)
def categoryes(request):
    categoryes = Category.objects.all()
    context = {'categoryes': categoryes}
    return render(request, 'categoryes.html', context)
def subcategoryes(request, id):
    subcategoryes = SubCategory.objects.filter(category_id = id)
    context = {'subcategoryes': subcategoryes}
    return render(request, 'categoryes.html', context)
def product_filter(request, id):
    products = Product.objects.filter(category_id = id)
    context = {'products': products}
    return render(request, 'categoryes.html', context)
# def all_product_filter(request, id):
#
