from django.db import models
from django.conf import settings
from shop.models import Item

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    wishlist = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.wishlist
    
    