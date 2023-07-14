from django.shortcuts import render,redirect
from .models import Product,Product_Image



# Create your views here.
def product(request, inp):
    print('aaaaaaaaaaa',inp)
    product=Product.objects.get(slug=inp)
    img=product.product_images.all()
    return render(request, "product/product.html",{"x":product,"y":img})

def show(request,inp):
    img=Product_Image.objects.get(identify_no=inp)
    return render(request,"product/details.html",{'a':img})



