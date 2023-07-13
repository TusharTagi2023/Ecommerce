from django.shortcuts import render,redirect
from .models import Product



# Create your views here.
def product(request, inp):
    product=Product.objects.get(product_name=inp)
    img=product.product_images.all()
    return render(request, "product/product.html",{"x":product,"y":img})
