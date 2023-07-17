from django.shortcuts import render,redirect
from .models import Product,Product_Image
from cart.models import Cart_items


# Create your views here.
def product(request, inp):
    print('aaaaaaaaaaa',inp)
    product=Product.objects.get(slug=inp)
    img=product.product_images.all()
    return render(request, "product/product.html",{"x":product,"y":img})

def show(request,inp):
    if request.method=='POST':
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        size=request.POST.get('size')
        quantity=request.POST.get('num')
        iddd=img.uid
        Cart_items(item_id=iddd,items_no=quantity,varient=size)






    img=Product_Image.objects.get(identify_no=inp)
    return render(request,"product/details.html",{'a':img})



