from django.urls import path
from . import views
urlpatterns=[
    path('login',views.login,name='login'),
    path('login',views.signup,name='signup')

]