from django.db import models
from base.models import BaseModel1



class Category (BaseModel1):
    category_name = models.CharField(max_length=100)
    slug=models.SlugField(unique=True, null=True, blank=True)
    category_image=models.ImageField(upload_to='catgories')



class Product (BaseModel1):
    product_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    slug=models.SlugField(unique=True, null=True, blank=True)
    price=models.IntegerField()
    product_description=models.TextField()



class Product_Image(BaseModel1):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image=models.ImageField(upload_to='product')
