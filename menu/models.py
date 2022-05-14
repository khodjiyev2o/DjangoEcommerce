from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=13)
    image = models.ImageField(upload_to='store/', null=True, blank=True)



    def __str__(self):
        return self.customer.username


class Product(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    digital = models.BooleanField(default=False)
    image = models.ImageField(upload_to='store/', null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, default=None, null=True, on_delete=models.SET_NULL)
    completed = models.BooleanField(default=False)
    date_ordered = models.DateField(auto_now=True)

    @property
    def overallprice(self):
        return sum([item.totalprice for item in self.orderitem_set.all()])

    @property
    def overallamount(self):
        return sum([item.quantity for item in self.orderitem_set.all()])

    def __str__(self):
        return str(self.customer)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateField(auto_now=True)
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)

    @property
    def totalprice(self):
        totalprice = self.product.price * self.quantity
        return totalprice
