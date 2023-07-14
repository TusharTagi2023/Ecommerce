from django.db import models
from base.models import BaseModel1
from django.utils.text import slugify



class Category (BaseModel1):
    category_name = models.CharField(max_length=100)
    slug=models.SlugField(unique=True, null=True, blank=True)
    category_image=models.ImageField(upload_to='catgories')

    def save(self, *args, **kwargs):
        self.slug=slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name



class Product (BaseModel1):
    product_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    slug=models.SlugField(unique=True, null=True, blank=True)
    price=models.IntegerField()
    product_description=models.TextField()


    def save(self, *args, **kwargs):
        self.slug=slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)




class Product_Image(BaseModel1):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    identify_no=models.BigIntegerField(default=0)
    image=models.ImageField(upload_to='product')
