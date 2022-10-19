from django.contrib import admin
from cart.models import Cart, Address, Order, Payment, Coupon, Refund

# Register your models here.
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)