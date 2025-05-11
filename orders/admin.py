from django.contrib import admin
from .models import Order, OrderItem, Status, Payment

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Status)
admin.site.register(Payment)
