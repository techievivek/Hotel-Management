from django.shortcuts import render,redirect
from .models import Customer
from django.contrib.auth.hashers import make_password
from django.contrib import messages
#mesages.info(request,'mail taken')
def user_login(request):
    return render(request,'login/user_login.html',{})
def manager_login(request):
    return render(request,'login/manager_login.html',{})
def user_signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        if Customer.objects.filter(username=username) or Customer.objects.filter(email=email):
           messages.warning(request,"Account already exist.")
        else:
            password=request.POST['password']
            address=request.POST['address']
            pin_code=request.POST['pin_code']
            profile_pic=request.FILES['profile_pic']
            phone_no=request.POST['phone_no']
            state=request.POST['state']
            error=[]
            if(len(username)<3):
                messages.warning(request,"Username Field must be greater than 3 character.")
            if(len(password)<5):
                messages.warning(request,"Password Field must be greater than 5 character.")
            if(len(email)==0):
                messages.warning(request,"Email field can't be empty")
            if(len(phone_no)!=10):
                messages.warning(request,"Valid Phone number is a 10 digit-integer.")
            if(len(error)==0):
                password_hash = make_password(password)
                customer=Customer(username=username,password=password_hash,email=email,phone_no=phone_no,address=address,state=state,pin_code=pin_code,profile_pic=profile_pic)
                customer.save()
                messages.info(request,"Account Created Successfully")
                redirect('user_signup')
            else:
                redirect('user_signup')
        
    else:
        redirect('user_signup')
    return render(request,'login/user_login.html',{})
def manager_signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        if Customer.objects.filter(username=username) or Customer.objects.filter(email=email):
           messages.warning(request,"Account already exist.")
        else:
            password=request.POST['password']
            address=request.POST['address']
            pin_code=request.POST['pin_code']
            profile_pic=request.FILES['profile_pic']
            phone_no=request.POST['phone_no']
            state=request.POST['state']
            error=[]
            if(len(username)<3):
                messages.warning(request,"Username Field must be greater than 3 character.")
            if(len(password)<5):
                messages.warning(request,"Password Field must be greater than 5 character.")
            if(len(email)==0):
                messages.warning(request,"Email field can't be empty")
            if(len(phone_no)!=10):
                messages.warning(request,"Valid Phone number is a 10 digit-integer.")
            if(len(error)==0):
                password_hash = make_password(password)
                customer=Customer(username=username,password=password_hash,email=email,phone_no=phone_no,address=address,state=state,pin_code=pin_code,profile_pic=profile_pic)
                customer.save()
                messages.info(request,"Account Created Successfully")
                redirect('user_signup')
            else:
                redirect('user_signup')
        
    else:
        redirect('user_signup')
    return render(request,'login/user_login.html',{})