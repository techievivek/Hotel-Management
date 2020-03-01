from django.shortcuts import render
def user_login(request):
    return render(request,'login/user_login.html',{})
def manager_login(request):
    return render(request,'login/manager_login.html',{})
def user_signup(request):
    return render(request,'login/manager_login.html',{})
def manager_signup(request):
    return render(request,'login/manager_login.html',{})
# Create your views here.
