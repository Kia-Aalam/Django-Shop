from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product, Size, Color


User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Cart {self.id} - {self.user.email}"

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)  
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ['cart', 'product', 'size', 'color']

    def __str__(self):
        return f"{self.product.title} - {self.size} - {self.color} - {self.quantity}"
    
    def save(self, *args, **kwargs):
        if not self.price or self.price == 0:
            if self.product and hasattr(self.product, 'price'):
                self.price = self.product.price
        super().save(*args, **kwargs)

    def get_total_price(self):
        if self.price is None:
            return 0
        return self.price * self.quantity