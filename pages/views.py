from django.shortcuts import render, redirect
from .forms import CouponForm
from pages.models import Wishlist
from django.contrib.auth.decorators import login_required


# Create your views here.
def faq_view(request):

    return render(request,'pages/faqs.html')


def about_us_view(request):

    return render(request, 'pages/about-us.html')

def contact_us_view(request):

    return render(request, 'pages/contact-us.html')

def checkout_view(request, method="POST"):

    coupon_form = CouponForm() 


    return render(request, 'pages/checkout.html', {"coupon_form" :coupon_form})

@login_required(login_url='/accounts/login')
def wishlist(request):
    wishlists = Wishlist.objects.filter(user=request.user, wishlist=True)
    return render(request, 'pages/wishlist.html', {'wishlists':wishlists})

@login_required
def add_to_wishlist(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = Wishlist.objects.get_or_create(
        item=item,
        user=request.user,
        wishlist=False
    )
    order_qs = Wishlist.objects.filter(user=request.user, wishlist=False)
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


