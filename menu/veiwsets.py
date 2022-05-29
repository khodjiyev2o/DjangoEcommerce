from rest_framework import mixins, viewsets
from .models import Product,Customer
from .serializers import ProductSerializer,CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class CustomerGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'