from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
# Create your tests here.


class CustomerTestCase(TestCase):

    def setUp(self):
        user =  User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')

    def test_contact_count(self):
        self.assertEqual(User.objects.count(),1)


