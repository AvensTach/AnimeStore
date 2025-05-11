from django.db import models
from products.models import Product
from accounts.models import User


# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return self.user.username + "`s Cart"


class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return self.cart.user.username + "`s Cart: " + self.product.name
