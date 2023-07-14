from django.urls import path
from .views import *

urlpatterns = [
    path("cart/items", cart ,name="Cart"),
]