from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart_view, name='home'),
]