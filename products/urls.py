from django.urls import path
from .views import *

urlpatterns = [
    path('DetailPage/<inp>', show ,name="Show_page"),
    path('Details/<inp>', product ,name="product_Detail_page"),
]