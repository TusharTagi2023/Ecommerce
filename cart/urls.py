from django.urls import path
from .views import *

urlpatterns = [
    path("cart", cart ,name="Cart"),
    path("Add_cart/<inp>", add_cart ,name="add_on"),

]

