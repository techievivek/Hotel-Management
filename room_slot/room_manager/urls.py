from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name="manager_dashboard"),
    path('new/',views.add_room,name="add_room"),
    path('update/<int:room_no>/',views.update_room,name="update_room"),

]
