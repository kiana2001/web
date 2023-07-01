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
    price_per_person_daily = models.FloatField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Passenger(models.Model):
    ssn = models.CharField(max_length=10)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HotelBooking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    checkin_date=models.DateTimeField(default=datetime.now())
    checkout_date=models.DateTimeField(default=datetime.now())
    check_out=models.BooleanField(default=False)
    no_of_guests=models.IntegerField(default=1)
    total_price=models.FloatField()
    passengers = models.ManyToManyField(Passenger)

    def __str__(self):
        return f"{self.user} reservation in {self.hotel}"
