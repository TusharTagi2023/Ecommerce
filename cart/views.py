from django.shortcuts import render,redirect
from products.models import Product_Image
from .models import Cart

# Create your views here.
def cart(request):
    usr=request.user
    all=Cart.objects.filter(user=usr)
    lst=[]
    for i in all:
        img=Product_Image.objects.get(uid=i.item_id)
        lst.append(img)
    
    return render(request, "cart/cart.html",{'x':all,'y':lst})

    