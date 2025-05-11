from django.db import models
from django.urls import reverse
from products.models import Product
from accounts.models import User


# Create your models here.
class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return "Status: " + self.status


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    provider = models.TextField()
    method = models.CharField(max_length=30)
    status = models.CharField(max_length=15)
    date = models.DateTimeField()
    amount = models.IntegerField()

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        # Note: We can add Payment Number as we did in Order to provide users with human-readable payments invoices
        return "Payment " + str(self.date) + "-" + self.provider[:3].capitalize()


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=15, unique=True)
    total_price = models.IntegerField()
    address = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return "Order " + self.order_number

    def get_absolute_url(self):
        return reverse("order", args=[self.order_number.upper()])


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return self.order.order_number + "`s Item: " + self.product.name
