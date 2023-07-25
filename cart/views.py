from django.shortcuts import render,redirect
from products.models import Product_Image
from .models import Cart,Items
from django.conf import settings
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def cart(request):
    usr=request.user
    all=Cart.objects.filter(user=usr, is_paid=False)
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



# Set your Stripe secret API key
stripe.api_key = 'sk_test_51NXKiQSFfzLEFTUhmGt6Z3cngIyi3ByROUjBzAgTNFMZd2j1Pd2qCUKMVO7UiaRVWmk1L5Zvu7axXzEEfHbjSaO9006FBdEyj4'

def create_checkout_session(request):
    if request.method == 'POST':
        try:

            sucss=reverse('success')
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price':'price_1NXKr4SFfzLEFTUhLD3V5oDO',  # Replace with your actual Price ID
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=request.build_absolute_uri(sucss),
                cancel_url=request.build_absolute_uri('/'),
            )
        except Exception as e:
            return HttpResponse(str(e), status=500)

        return redirect(checkout_session.url, code=303)
    else:
        return HttpResponse("Method not allowed", status=405)


def Success(request):
    print(request.__dict__)
    user=request.user
    carts=Cart.objects.filter(user=user)
    for i in carts:
        i.is_paid=True
        i.save()
    return redirect('Index')

def delivery(request):
    usr=request.user
    all=Cart.objects.filter(user=usr, is_paid=True)
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
    return render(request, "cart/Delivery.html",{'var':mylist,'price':price})




