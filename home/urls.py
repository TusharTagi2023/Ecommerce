from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page,name="Index"),
]