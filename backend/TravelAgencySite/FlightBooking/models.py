from django.db import models

from django.db import models
from django.contrib.auth.models import User

from Users.models import User

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    airport = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.airport} airport"   

class Flight(models.Model):

    airline = models.CharField(max_length=30)
    flight_number = models.CharField(max_length=10)
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrivals')
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()

    price = models.DecimalField(decimal_places=2, max_digits=10)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.airline} {self.flight_number} - {self.origin} to {self.destination}"

class FlightReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='FlightReservations')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    is_round_trip = models.BooleanField(default=False)
    return_date = models.DateField(null=True, blank=True)
    num_adults = models.PositiveSmallIntegerField(verbose_name = "number of adults")
    num_children = models.PositiveSmallIntegerField(verbose_name = "number of kids")
    return_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='return_reservations', null=True, blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default = 0)

    def __str__(self):
        return f"{self.user} - {self.flight}"

class Passenger(models.Model):
    reservation = models.ForeignKey(FlightReservation, on_delete=models.CASCADE, related_name='passengers')
    ssn = models.CharField(max_length=10)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_adult = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

