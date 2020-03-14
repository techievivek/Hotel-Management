from django.test import TestCase
from .models import Rooms
from .models import Booking
from login.models import Customer, RoomManager
import datetime

class RoomsTestCases(TestCase):
    def setUp(self):
        RoomManager.objects.create(username='vivek')
        manager=RoomManager.objects.get(username='vivek')
        Rooms.objects.create(manager=manager,room_no=300,room_type='Deluxe',price=3000,is_available=True,no_of_days_advance=10,start_date='2020-03-20')
        Rooms.objects.create(manager=manager,room_no=301,room_type='Super Deluxe',price=5000,is_available=True,no_of_days_advance=15,start_date='2020-03-26')

    def test_room_no(self):
        """Rooms with room_no are correctly identified"""
        room1 = Rooms.objects.get(room_no='300')
        room2 = Rooms.objects.get(room_no='301')
        self.assertEqual(room1.room_no, '300')
        self.assertEqual(room2.room_no, '301')
    def test_room_type(self):
        """Rooms with room_no are correctly identified"""
        room1 = Rooms.objects.get(room_type='Deluxe')
        room2 = Rooms.objects.get(room_type='Super Deluxe')
        self.assertEqual(room1.room_type, 'Deluxe')
        self.assertEqual(room2.room_type, 'Super Deluxe')
    def test_price(self):
        """Rooms with price are correctly identified"""
        room1 = Rooms.objects.get(price=3000)
        room2 = Rooms.objects.get(price=5000)
        self.assertEqual(room1.price, 3000)
        self.assertEqual(room2.price, 5000)