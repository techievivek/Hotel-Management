from django.test import TestCase
from .models import Customer
from .models import RoomManager
from booking.models import Booking, Rooms
import datetime

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username='vivek',email='vray6640@gmail.com',pin_code=799046,phone_no='8794173921')
        Customer.objects.create(username='vikas',email='vikas@gmail.com',pin_code=799046,phone_no='9090909090')
    def test_customer_username(self):
        customer1=Customer.objects.get(phone_no='8794173921')
        customer2=Customer.objects.get(username='vikas')
        self.assertEqual(customer1.username,'vivek')
        self.assertEqual(customer2.username,'vikas')
    def test_customer_email(self):
        customer1=Customer.objects.get(email='vray6640@gmail.com')
        customer2=Customer.objects.get(username='vikas')
        self.assertEqual(customer1.email,'vray6640@gmail.com')
        self.assertEqual(customer2.email,'vikas@gmail.com')



