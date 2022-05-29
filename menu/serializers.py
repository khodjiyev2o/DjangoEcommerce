from .models import Product, OrderItem, Customer
from rest_framework import serializers
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'username', 'first_name', 'last_name','email','is_staff']


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    url =  serializers.HyperlinkedIdentityField(
        view_name='products',
        lookup_field='pk'
    )


    class Meta:
        model = Customer
        fields = ['customer','url','phone', 'image', 'id', 'user']


    def get_user(self, obj):
        user = User.objects.filter(
            username=obj.customer)
        serializer = UserSerializer(user, many=True)

        return serializer.data
