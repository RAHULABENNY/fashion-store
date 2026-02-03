from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

# Create your models here.
class Clothitems(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(upload_to='clothitems/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    is_avilable=models.BooleanField(default=True)

    def __str__(self):
        return self.name