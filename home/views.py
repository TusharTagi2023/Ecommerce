from django.shortcuts import render,redirect
from products.models import Category

# Create your views here.
def index_page(request):
    products=Category.objects.all()
    return render(request, "home/index.html",{'data':products})
