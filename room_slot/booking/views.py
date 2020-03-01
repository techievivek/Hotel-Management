from django.shortcuts import render
from .models import Contact
def index(request):
    return render(request,'booking/index.html',{})
def book(request):
    return render(request,'booking/book.html',{})
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
