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
        return redirect('/')
    return render(request,"product/details.html",{'a':img})


def adding_to_cart(usr,size,num,idd):
    try:
        id=Cart.objects.get(item_id=idd)
        chmg=Items.objects.get(cart=id)
        num=int(num)+chmg.items_no
        size=size+','+chmg.varient

        id.delete()
        Items(cart=id,items_no=num,varient=size).save()
    except:
        Cart(user=usr,item_id=idd).save()
        id=Cart.objects.get(item_id=idd)
        Items(cart=id,items_no=num,varient=size).save()
        return




