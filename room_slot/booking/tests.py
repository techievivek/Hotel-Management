from django.test import TestCase,Client
from .models import Rooms
from .models import Booking
from login.models import Customer, RoomManager
import datetime
from django.urls import reverse
class RoomsTestCases(TestCase):
    def setUp(self):
        RoomManager.objects.create(username='vivek')
        manager=RoomManager.objects.get(username='vivek')
        Rooms.objects.create(manager=manager,room_no=300,room_type='Deluxe',price=3000,is_available=True,no_of_days_advance=10,start_date='2020-03-20')
        Rooms.objects.create(manager=manager,room_no=301,room_type='Super Deluxe',price=5000,is_available=True,no_of_days_advance=15,start_date='2020-03-26')

    def test_room_no(self):
        room1 = Rooms.objects.get(room_no='300')
        room2 = Rooms.objects.get(room_no='301')
        self.assertEqual(room1.room_no, '300')
        self.assertEqual(room2.room_no, '301')
    def test_room_type(self):
        room1 = Rooms.objects.get(room_type='Deluxe')
        room2 = Rooms.objects.get(room_type='Super Deluxe')
        self.assertEqual(room1.room_type, 'Deluxe')
        self.assertEqual(room2.room_type, 'Super Deluxe')
    def test_price(self):
        room1 = Rooms.objects.get(price=3000)
        room2 = Rooms.objects.get(price=5000)
        self.assertEqual(room1.price, 3000)
        self.assertEqual(room2.price, 5000)
class BookingTestCases(TestCase):
    def setUp(self):
        RoomManager.objects.create(username='rahul')
        manager=RoomManager.objects.get(username='rahul')
        Customer.objects.create(username='vivek',pin_code=799046)
        Customer.objects.create(username='vikas',pin_code=799046)
        Rooms.objects.create(room_no='300',no_of_days_advance=10,start_date='2020-03-09',manager=manager)
        user=Customer.objects.get(username='vivek')
        user1=Customer.objects.get(username='vikas')
        room=Rooms.objects.get(room_no='300')
        Booking.objects.create(user_id=user,room_no=room,amount=10000,start_day='2020-03-10',end_day='2020-03-10')
        Booking.objects.create(user_id=user1,room_no=room,amount=5000,start_day='2020-03-26',end_day='2020-03-28')

    def test_booking_username(self):
        user=Customer.objects.get(username='vivek')
        booking1 = Booking.objects.get(user_id=user)
        user1=Customer.objects.get(username='vikas')
        booking2 = Booking.objects.get(user_id=user1)
        self.assertEqual(booking1.user_id.username, 'vivek')
        self.assertEqual(booking2.user_id.username, 'vikas')
    def test_booking_amount(self):
        booking1 = Booking.objects.get(amount=10000)
        booking2 = Booking.objects.get(amount=5000)
        self.assertEqual(booking1.amount, 10000)
        self.assertEqual(booking2.amount, 5000)
    def test_booking_roomManager(self):
        booking = Booking.objects.get(amount=5000)
        self.assertEqual(booking.room_no.manager.username, 'rahul')
class IndexPageViewTest(TestCase):
    def setUp(self):
        self.client=Client()
        self.index_url=reverse('index')
    def test_index_view(self):
        response=self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'booking/index.html')