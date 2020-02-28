from django.shortcuts import render
def index(request):
    return render(request,'booking/index.html',{})
def book(request):
    return render(request,'booking/book.html',{})
# Create your views here.
