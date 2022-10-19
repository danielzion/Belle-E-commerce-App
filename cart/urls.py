from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    add_to_cart,
    CartView,
    delete_cart,
)

app_name = 'cart'

urlpatterns = [
    # path('add', views.add_to_cart, name='add_to_cart'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('delete/<slug>/', views.delete_cart, name='delete_cart'),
    path('update', views.update_cart, name='update_cart'),
    path('', views.CartView, name='home'),
]
