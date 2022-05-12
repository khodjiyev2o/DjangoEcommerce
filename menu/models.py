from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=13)


    def __str__(self):
        return self.customer.username


class Product(models.Model):
    name = models.TextField()
    price = models.CharField(max_length=13)
    digital = models.BooleanField(default=False)
    image = models.ImageField(upload_to='store/', null=True, blank=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    customer=models.ForeignKey(Customer,default=None,null=True,on_delete=models.SET_NULL)
    date_ordered=models.DateField(auto_now=True)
    product=models.ForeignKey(Product,default=None,null=True,on_delete=models.SET_NULL)
    quantity=models.IntegerField(max_length=10)


    def __str__(self):
        return self.product.name
    