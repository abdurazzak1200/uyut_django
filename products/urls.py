from django.urls import path
from .views import index, product_deteil, contact, categoryes, subcategoryes, product_filter
urlpatterns = [
    path('', index, name='index'),
    path('product_deteil/<int:id>/', product_deteil, name='product_deteil'),
    path('contact/', contact, name='contact'),
    path('categoryes/', categoryes, name='categoryes'),
    path('subcategoryes/<int:id>', subcategoryes, name='subcategoryes'),
    path('product_filter/<int:id>', product_filter, name='product_filter')
]