from django.shortcuts import render,redirect
from .models import Contact
from .models import Rooms,Booking
from login.models import Customer
from django.contrib import messages
import datetime
def index(request):
    return render(request,'booking/index.html',{})
def contact(request):
    if request.method=="GET":
     return render(request,"contact/contact.html",{})
    else:
     username=request.POST['name']
     email=request.POST['email']
     message=request.POST['message']
     data=Contact(name=username,email=email,message=message)
     data.save()
     return render(request,"contact/contact.html",{'message':'Thank you for contacting us.'})
def book(request):
    if request.method=="POST":
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        request.session['start_date']=start_date
        request.session['end_date']=end_date
        start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
        end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
        no_of_days=(end_date-start_date).days
        data=Rooms.objects.filter(is_available=True,no_of_days_advance__gte=no_of_days,start_date__lte=start_date)
        request.session['no_of_days']=no_of_days
        return render(request,'booking/book.html',{'data':data})
    else:
        return redirect('index')
def book_now(request,id):
    if request.session.get("username",None):
        if request.session.get("no_of_days",1):
            no_of_days=request.session['no_of_days']
            start_date=request.session['start_date']
            end_date=request.session['end_date']
            request.session['room_no']=id
            data=Rooms.objects.get(room_no=id)
            bill=data.price*int(no_of_days)
            request.session['bill']=bill
            roomManager=data.manager.username
            return render(request,"booking/book-now.html",{"no_of_days":no_of_days,"room_no":id,"data":data,"bill":bill,"roomManager":roomManager,"start":start_date,"end":end_date})
        else:
            return redirect("index")
    else:
        next="book-now/"+id
        return render(request,"login/user_login.html",{"next":next})
def book_confirm(request):
    room_no=request.session['room_no']
    start_date=request.session['start_date']
    end_date=request.session['end_date']
    username=request.session['username']
    user_id=Customer.objects.get(username=username)
    room=Rooms.objects.get(room_no=room_no)
    amount=request.session['bill']
    start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
    end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
    data=Booking(room_no=room,start_day=start_date,end_day=end_date,amount=amount,user_id=user_id)
    data.save()
    del request.session['start_date']
    del request.session['end_date']
    del request.session['bill']
    del request.session['room_no']
    messages.info(request,"Room has been successfully booked")
    return redirect('user_dashboard')

            



    
