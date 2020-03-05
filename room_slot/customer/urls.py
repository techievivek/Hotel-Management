from django.urls import path
from . import views
urlpatterns=[
    path('',views.dashboard,name='user_dashboard'),
    path('details/<int:id>/<int:booking_id>',views.details,name='user_details')
]