from django.contrib.auth.models import User
from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class Restaurant(models.Model): ...


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart



class OrderItem(models.Model): ...


class Order(models.Model): ...


class Courier(models.Model): ...


class Address(models.Model): ...


class Payment(models.Model): ...
