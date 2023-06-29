from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    details = models.TextField()
    expiration_date = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(default='no_image_avail.png', upload_to='product-pictures')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


##########CARTS##############
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, through='CartItem')

    def get_total_quantity(self):
        return self.cart_items.aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0

    def get_total_price(self):
        return self.cart_items.aggregate(total_price=models.Sum(models.F('quantity') * models.F('product__price')))['total_price'] or 0

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)