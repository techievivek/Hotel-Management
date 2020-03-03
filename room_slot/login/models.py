from django.db import models
from PIL import Image
class Customer(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    phone_no=models.IntegerField()
    address=models.TextField()
    state=models.CharField(max_length=30)
    pin_code=models.IntegerField()
    def __str__(self):
        return "Details of Customer "+self.username
class RoomManager(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    phone_no=models.IntegerField()
    gender=models.CharField(max_length=20)
    def __str__(self):
        return "Details of Room Manager "+self.username

