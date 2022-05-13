from . import models
import django_filters
from django_filters import CharFilter


class ProductFilter(django_filters.FilterSet):
    product = CharFilter(field_name="name", lookup_expr='icontains')
    price = CharFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = models.Product
        fields = ['product', 'price']
