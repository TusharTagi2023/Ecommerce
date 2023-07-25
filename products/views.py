from django.shortcuts import render,redirect
from .models import Product,Product_Image
from cart.models import Items,Cart
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def product(request, inp):
    prod=Product.objects.get(slug=inp)
    img=prod.product_images.all()
    return render(request, "product/product.html",{"x":prod,"y":img})

def show(request,inp):
    img=Product_Image.objects.get(identify_no=inp)
    if request.method=='POST':
        if request.user.is_authenticated:
            size=request.POST.get('size')
            quantity=request.POST.get('num')
            iddd=img.uid
            user=request.user
            adding_to_cart(user,size,quantity,iddd)
            return redirect('/')
        return redirect('LogIn')
    return render(request,"product/details.html",{'a':img})


def adding_to_cart(usr,size,num,idd):
    try:
        id=Cart.objects.filter(user=usr, is_paid=False)[0]
        chmg=Items.objects.get(cart=id)
        num=int(num)+chmg.items_no + 0
        size=size+','+chmg.varient
        id.delete()
        Items(cart=id,items_no=num,varient=size).save()
    except:
        Cart(user=usr,item_id=idd).save()
        id=Cart.objects.filter(user=usr, is_paid=False)[0]
        Items(cart=id,items_no=num,varient=size).save()
        return
    

def all_product(request):
    prod=Product.objects.all()
    lst=[]
    for i in prod:
        img=i.product_images.all()
        lst.append(img)
    return render(request, "product/All_products.html",{"y":lst})

def search_product(request):
    if request.method=='POST':
        inp =request.POST.get('search_content')
        products = Product.objects.filter(Q(product_name__icontains=inp) | Q(category__category_name__icontains=inp))
        lst=[]
        for i in products:
            img=i.product_images.all()
            lst.append(img)
        return render(request, "product/All_products.html",{"y":lst})
    return redirect('/')




