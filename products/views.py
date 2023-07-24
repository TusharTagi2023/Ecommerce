from django.shortcuts import render,redirect
from .models import Product,Product_Image
from cart.models import Items,Cart
from django.contrib.auth.decorators import login_required


# Create your views here.
def product(request, inp):
    print('aaaaaaaaaaa',inp)
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
        id=Cart.objects.get(item_id=idd)
        chmg=Items.objects.get(cart=id)
        num=int(num)+chmg.items_no + 0
        size=size+','+chmg.varient
        id.delete()
        Items(cart=id,items_no=num,varient=size).save()
    except:
        Cart(user=usr,item_id=idd).save()
        id=Cart.objects.get(item_id=idd)
        Items(cart=id,items_no=num,varient=size).save()
        return




