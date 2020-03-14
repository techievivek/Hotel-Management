from rest_framework import viewsets
from login.models import Customer
from booking.models import Booking,Rooms
from . import serializers

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.UserSerializer

class RoomsViewset(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = serializers.RoomsSerializer

class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer