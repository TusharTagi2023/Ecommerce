from django.shortcuts import render,redirect
from products.models import Product_Image
from .models import Cart,Items
from razorpay import Client
from django.conf import settings


# Create your views here.
def cart(request):
    usr=request.user
    all=Cart.objects.filter(user=usr)
    lst=[]
    lst1=[]
    price=0
    for i in all:
        img=Product_Image.objects.get(uid=i.item_id)
        lst.append(img)
        temp=i.cart_items.get()
        lst1.append(temp)
        price=temp.items_no*img.product.price + price
    mylist = zip(lst, lst1)
    return render(request, "cart/cart.html",{'var':mylist,'price':price})

def remov(request,inp):
    dlt=Cart.objects.get(item_id=inp)
    dlt.delete()
    return redirect('Cart')


def create_order(request):
    client = Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
    amount = 10000  # Amount in paise (Example: ₹100)
    currency = 'INR'
    receipt = 'order_rhzjghhjghjgfghfghgh'  # Unique order ID or receipt
    return render(request, 'cart/payment.html', {'amount':amount, 'currency': currency, 'receipt': receipt, 'payment_capture': 1})

    