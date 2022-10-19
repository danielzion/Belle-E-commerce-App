from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'pages'

urlpatterns = [
    path('faqs/', views.faq_view, name='faqs'),
    path('about-us/', views.about_us_view, name='about-us'),
    path('contact-us/', views.contact_us_view, name='contact-us'),
    path('checkout/', views.checkout_view, name='checkout'),
    path("wishlist", views.wishlist, name="wishlist"),
]