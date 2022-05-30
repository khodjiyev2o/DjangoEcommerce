from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

def validate_name(self, value):
    qs = Product.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"this {value} already exists")
    return value


