from . import models
import django_filters
from django_filters import CharFilter
from django import forms


class ProductFilter(django_filters.FilterSet):
    product = CharFilter(field_name="name", lookup_expr='icontains',label='',
                         widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Search a product'}))

    # price = CharFilter(field_name="price", lookup_expr='lte', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Product
        fields = ['product']
