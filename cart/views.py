from django.shortcuts import render,redirect
from products.models import Product_Image,Product

# Create your views here.
def cart(request):
    return render(request, "cart/cart.html")

def add_cart(request,inp):
    img= Product_Image.objects.get(uid=inp)
    print('*****************************************************',type(inp))
    return render(request,"cart/cart.html",{'x':img})
    