from django.shortcuts import render
from login.models import Customer
from booking.models import Booking
def dashboard(request):
  if request.session.get("username",None):
      username=request.session['username']
      data=Customer.objects.get(username=username)
      booking_data=Booking.objects.filter(user_id=data)
      return render(request,"user_dash/index.html",{"data":data})
  else:
      return redirect("user_login")
# Create your views here.
