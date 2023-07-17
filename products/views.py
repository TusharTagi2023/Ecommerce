from django.shortcuts import render,redirect
from .models import Product,Product_Image
from cart.models import Items,Cart
from django.contrib.auth.decorators import login_required


# Create your views here.
def product(request, inp):
    print('aaaaaaaaaaa',inp)
    product=Product.objects.get(slug=inp)
    img=product.product_images.all()
    return render(request, "product/product.html",{"x":product,"y":img})

def show(request,inp):
    img=Product_Image.objects.get(identify_no=inp)
    if request.method=='POST':
        size=request.POST.get('size')
        quantity=request.POST.get('num')
        iddd=img.uid
        user=request.user
        adding_to_cart(user,size,quantity,iddd)

    return render(request,"product/details.html",{'a':img})

@login_required
def adding_to_cart(usr,size,num,idd):
    Cart(user=usr,item_id=idd).save()
    print('Workinnnnnnnnnnnnnnnnnnnnnnnnng')
    Cart.cart_items(items_no=num,varient=size).save()




