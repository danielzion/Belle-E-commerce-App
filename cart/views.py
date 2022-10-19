from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from cart.models import Cart, Order
from shop.models import Item
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.utils import timezone


@login_required(login_url='/accounts/login')
def CartView(request):
    carts = Cart.objects.filter(user=request.user, ordered=False)
    # subtotal = 0 
    # for cart in carts:
    #     if cart.item.discount_price:
    #         for i in cart.get_total_discount_item_price:
    #             subtotal =+ i 
    #     else:
    #         for i in cart.get_total_item_price:
    #             subtotal =+ i 
     


    return render(request, 'cart/cart.html', {'carts':carts, 
        # 'subtotal':subtotal
        })



@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("cart:home")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("cart:home")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("cart:home")

        return response

@login_required
def delete_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the cart
        if order.items.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("cart:home")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("cart:home", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("cart:home", slug=slug)




@login_required
def update_cart(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form']
    # item = get_object_or_404(Item)
    # order_item, created = Cart.objects.get_or_create(
    #     item=item,
    #     user=request.user,
    #     ordered=False
    # )
    # order_qs = Order.objects.filter(user=request.user, ordered=False)
    # if order_qs.exists():
    #     order = order_qs[0]
    #     # check if the order item is in the order
    #     if order.items.filter(item__slug=item.slug).exists():
    #         order_item.quantity += 1
    #         order_item.save()
    #         messages.info(request, "This item quantity was updated.")
    #         return redirect("cart:home")
    #     else:
    #         order.items.add(order_item)
    #         messages.info(request, "This item was added to your cart.")
    #         return redirect("cart:home")
    # else:
    #     ordered_date = timezone.now()
    #     order = Order.objects.create(
    #         user=request.user, ordered_date=ordered_date)
    #     order.items.add(order_item)
    #     messages.info(request, "This item was added to your cart.")
    #     return redirect("cart:home")

        return response

