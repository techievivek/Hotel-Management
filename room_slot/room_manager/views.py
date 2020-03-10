from django.shortcuts import render,redirect
from login.models import RoomManager
from booking.models import Booking,Rooms
from datetime import date
from django.contrib import messages
import datetime
def dashboard(request):
  if not request.session.get('username',None):
      return redirect('manager_login')
  if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
  if request.session.get('username',None) and request.session.get('type',None)=='manager':
      username=request.session['username']
      data=RoomManager.objects.get(username=username)
      room_data=data.rooms_set.all()
      booked=room_data.filter(is_available=False).count()
      print(booked)
      return render(request,"manager_dash/index.html",{"room_data":room_data,"manager":data,"booked":booked})
  else:
      return redirect("manager_login")
def add_room(request):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.method=="GET":
        return render(request,"manager_dash/add-room.html",{})
    else:
            room_no=request.POST['room_no']
            room_type=request.POST['room_type']
            price=request.POST['price']
            room_image=request.FILES.get('room_image',None)
            no_of_days_advance=request.POST['no_of_days_advance']
            start_day=request.POST['start_day']
            error=[]
            if(len(room_no)<1):
                error.append(1)
                messages.warning(request,"Room No Field must be atleast 3 digit like 100.")
            if(len(room_type)<5):
                error.append(1)
                messages.warning(request,"Select a valid Room Type.")
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter price")
            if(len(no_of_days_advance)<1):
                error.append(1)
                messages.warning(request,"Please add valid no of days a user can book room in advance.")
            if(len(start_day)<3):
                error.append(1)
                messages.warning(request,"Please add the starting day")
            if(not len(error)):
                manager=request.session['username']
                manager=RoomManager.objects.get(username=manager)
                room=Rooms(room_no=room_no,room_type=room_type,price=price,no_of_days_advance=no_of_days_advance,start_date=datetime.datetime.strptime(start_day, "%d %B, %Y").date(),room_image=room_image,manager=manager)
                room.save()
                messages.info(request,"Room Added Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-room/new/')
def update_room(request,room_no):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    room=Rooms.objects.get(room_no=room_no)
    if request.method=="GET":
        return render(request,"manager_dash/edit-room.html",{"room":room})
    else:
            price=request.POST['price']
            no_of_days_advance=request.POST['no_of_days_advance']
            error=[]
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter correct price")
            if(len(no_of_days_advance)<1):
                error.append(1)
                messages.warning(request,"Please add valid no of days a user can book room in advance.")
            if(not len(error)):
                manager=request.session['username']
                manager=RoomManager.objects.get(username=manager)
                room.price=price
                room.no_of_days_advance=no_of_days_advance
                room.save()
                messages.info(request,"Room Data Updated Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-room/update/'+room.room_no,{"room":room})

