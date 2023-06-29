from django.db import models
from shop.models import Product

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    code = models.CharField(max_length=16)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return self.code