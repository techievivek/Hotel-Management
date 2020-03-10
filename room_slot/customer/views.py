from django.shortcuts import render,redirect
from login.models import Customer
from booking.models import Booking
import datetime
def dashboard(request):
  if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
  if request.session.get('username',None) and request.session.get('type',None)=='customer':
      username=request.session['username']
      data=Customer.objects.get(username=username)
      booking_data=Booking.objects.filter(user_id=data).order_by('-id')
      counts=booking_data.filter(end_day__lt=datetime.datetime.now()).count()
      available=len(booking_data)-counts
      return render(request,"user_dash/index.html",{"data":booking_data,"count":counts,"available":available})
  else:
      return redirect("user_login")
def details(request,id,booking_id):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    try:
        booking_data=Booking.objects.get(id=booking_id)
        user=Customer.objects.get(id=id)
        return render(request,"user_dash/details.html",{"user":user,"booking_data":booking_data})
    except:
        return redirect("/manager/dashboard1/")

