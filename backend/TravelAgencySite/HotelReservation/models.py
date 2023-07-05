from django.db import models
from Users.models import User
from datetime import datetime, timedelta

class City(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} : {self.country}"   

class Hotel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='location')
    address = models.CharField(max_length=500)
    stars = models.IntegerField()
    def __str__(self):
        return f"id: {self.id}, {self.name}"

class Passenger(models.Model):
    ssn = models.CharField(max_length=10)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Room(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    room_number = models.IntegerField()
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE, related_name="rooms")
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default = True)

    def __str__(self):
        return f"id: {self.id}, {self.room_number} {self.hotel}"

class HotelBooking(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    checkin_date=models.DateTimeField(default=datetime.now())
    checkout_date=models.DateTimeField(default=datetime.now())
    check_out=models.BooleanField(default=False)
    no_of_guests=models.IntegerField(default=1)
    total_price=models.FloatField()
    passengers = models.ManyToManyField(Passenger)

    def __str__(self):
        return f"{self.user} reservation in {self.room}"
