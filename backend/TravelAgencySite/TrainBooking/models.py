from django.db import models

from django.db import models
from django.contrib.auth.models import User
from Users.models import User
from FlightBooking.models import City

class Train(models.Model):

    company = models.CharField(max_length=30)
    train_number = models.CharField(max_length=10)
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrivals')
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()

    price = models.DecimalField(decimal_places=2, max_digits=10)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.company} {self.train_number} - {self.origin} to {self.destination}"

class Passenger(models.Model):
    ssn = models.CharField(max_length=10)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_adult = models.BooleanField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TrainReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='FlightReservations')
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    is_round_trip = models.BooleanField(default=False)
    num_adults = models.PositiveSmallIntegerField(verbose_name = "number of adults")
    num_children = models.PositiveSmallIntegerField(verbose_name = "number of kids")
    return_train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='return_reservations', null=True, blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    passengers = models.ManyToManyField(Passenger)

    def __str__(self):
        return f"{self.user} - {self.flight}"

