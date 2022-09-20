from django.shortcuts import render, redirect

# Create your views here.
def cart_view(request):

    return render(request,'cart/cart.html')