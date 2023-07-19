from django.urls import path
from .views import *

urlpatterns = [
    path("cart", cart ,name="Cart"),
    path("Dlt/<inp>", remov ,name="move"),
]

