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
        fields = ['id','manager', 'room_no', 'room_type', 'is_available','price','no_of_days_advance','start_date','room_image']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','room_no', 'user_id', 'start_day', 'end_day','amount','booked_on']