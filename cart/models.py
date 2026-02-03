from django.db import models
from django.contrib.auth.models import User
from menu.models import Clothitems 

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Clothitems, on_delete=models.CASCADE) # Ensure this is aligned!
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"