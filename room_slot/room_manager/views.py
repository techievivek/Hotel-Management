from django.shortcuts import render,redirect
from login.models import RoomManager
from booking.models import Booking
from datetime import date
def dashboard(request):
  if request.session.get("username",None):
      username=request.session['username']
      data=RoomManager.objects.get(username=username)
      room_data=data.rooms_set.all()
      booked=room_data.filter(is_available=False).count()
      print(booked)
      return render(request,"manager_dash/index.html",{"room_data":room_data,"manager":data,"booked":booked})
  else:
      return redirect("manager_login")
def add_room(request):
    return render(request,"manager_dash/add-room.html",{})
# Create your views here.
