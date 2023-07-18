from django.urls import path
from .views import *

urlpatterns = [
    path('login_page', login_page,name="LogIn"),
    path('register', user_regs, name="Register"),
    path("Validatiod/<email_token>",accont_activation, name="activation_page"),
    path('lOg',logout_view ,name="LoG"),
]