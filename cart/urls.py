from django.urls import path
from .views import *

urlpatterns = [
    path("cart", cart ,name="Cart"),
    path("paymnt", create_checkout_session ,name="Payment"),
    path("Dlt/<inp>", remov ,name="move"),
    
]

