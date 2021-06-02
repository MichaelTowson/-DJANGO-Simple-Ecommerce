from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooelanField(default=False)
    
    def __str__(self):
        return self.title

#This model represents the item that someone has in their cart.
class OrderItem(models.Model):
    order = models.ForeignKey("Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveItnegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_Date = models.DateTimeField(blank=True, null=True) #value gets set after order has been paid for.