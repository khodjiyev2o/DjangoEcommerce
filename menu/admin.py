from django.contrib import admin
from .models import Customer, Product, OrderItem, Order
# Register your models here.
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Customer


class UserAdmin(admin.ModelAdmin):
    model = User
    fields =  ["username"]
    inlines = [ProfileInline]


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
