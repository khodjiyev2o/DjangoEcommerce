from django.test import TestCase
from .models import Customer, User


# Create your tests here.


class CustomerTestCase(TestCase):

    def setup(self):
        user = User.objects.create_user(username='testuser', password='12345')
        customer1 = Customer.objects.create(first_name ='testuser', phone="2249735")


    def customer_number_test(self):

        customer1 = Customer.objects.first()

        self.assertEqual(customer1.allcustomers, int(User.objects.all().count() - 1) )


