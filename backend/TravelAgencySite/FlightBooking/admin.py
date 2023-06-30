from django.contrib import admin
from .models import Flight,FlightReservation, Passenger, City

admin.site.register(Flight)
admin.site.register(FlightReservation)
admin.site.register(Passenger)
admin.site.register(City)



