from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

default_value = timezone.now


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='category_images/', default='category_images/default.jpg')

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # You can specify a different upload path if needed
    quantity = models.IntegerField(default=0)  # Specify your desired default value here
    vendor = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    original_price = models.FloatField(blank=False, default=0.0)
    selling_price = models.FloatField(blank=False, default=0.0)
    status = models.BooleanField(default=False, help_text='0-show, 1-Hidden')
    trending = models.BooleanField(default=False, help_text='0-default, 1-Trending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


