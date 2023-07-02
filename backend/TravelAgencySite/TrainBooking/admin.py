from django.contrib import admin
from .models import Train,TrainReservation, Passenger

admin.site.register(Train)
admin.site.register(TrainReservation)
admin.site.register(Passenger)