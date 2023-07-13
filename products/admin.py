from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)



class ProdImg(admin.StackedInline):
    model=Product_Image

class ProdAd(admin.ModelAdmin):
    inlines=[ProdImg]

admin.site.register(Product, ProdAd)
admin.site.register(Product_Image)

