from rest_framework import serializers
from login.models import Customer
from booking.models import Booking,Rooms
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username', 'password', 'email', 'state','pin_code','address','profile_pic']
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id','username', 'password', 'email', 'state','pin_code','address','profile_pic']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','username', 'password', 'email', 'state','pin_code','address','profile_pic']