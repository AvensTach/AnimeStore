from django.contrib import admin
from .models import Product, Category, Media

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Media)
