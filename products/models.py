from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET(0))

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name.capitalize()

    def get_absolute_url(self):
        return reverse('category', args=[self.name.lower()])

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name.capitalize()

class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    alternative_text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    media = models.ImageField(upload_to="media/")

    class Meta:
        verbose_name = "Media File"
        verbose_name_plural = "Media Files"

    def __str__(self):
        return "Product Image: " + self.product.name.capitalize()