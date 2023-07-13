from django.shortcuts import render,redirect

# Create your views here.
def index_page(request):
    return render(request, "home/index.html",{'data':[1,2,3,4,5,67,8]})
