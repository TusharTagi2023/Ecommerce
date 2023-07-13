from django.urls import path
from .views import *

urlpatterns = [
    path('<inp>', product ,name="product_Detail_page"),
]