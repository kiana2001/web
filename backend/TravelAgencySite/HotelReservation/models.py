from django.db import models
from Users.models import User
from datetime import datetime, timedelta

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} : {self.country}"   

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    city= models.ForeignKey(City, on_delete=models.CASCADE, related_name='location')
    address = models.CharField(max_length=500)
    stars = models.IntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    room_no=models.IntegerField(default=101)
    hotel=models.ForeignKey(Hotel,null=True,on_delete=models.CASCADE)
    room_type=models.CharField(max_length=200,default='standard')
    price=models.FloatField()
    is_available=models.BooleanField(default=True)
    no_of_beds=models.IntegerField(default=2)
    description = models.TextField()
    def __str__(self):
        return f"Room:{self.room_no} of {self.hotel} hotel"  

class HotelBooking(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    checkin_date=models.DateTimeField(default=datetime.now())
    checkout_date=models.DateTimeField(default=datetime.now())
    check_out=models.BooleanField(default=False)
    no_of_guests=models.IntegerField(default=1)
    total_price=models.FloatField()

    def __str__(self):
        return f"{self.user} reservation in {self.hotel}" 

