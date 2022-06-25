from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
# Create your tests here.


class CustomerTestCase(TestCase):
    def setUp(self):

        user =  User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        product = Product.objects.create(name="book",price=15,digital=False)


    def test_contact_count(self):
        self.assertEqual(User.objects.count(),1)


    def test_product_counter(self):
        self.assertEqual(Product.objects.count(),1)
