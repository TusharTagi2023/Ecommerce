from django.db import models
from base.models import BaseModel1
from django.contrib.auth.models import User


class Cart(BaseModel1):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_cart')
    item_id= models.CharField(max_length=100,null=True, blank=True)


class Items(BaseModel1):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='cart_items')
    items_no=models.IntegerField(null=True, blank=True)
    varient=models.CharField(max_length=10,null=True, blank=True)

