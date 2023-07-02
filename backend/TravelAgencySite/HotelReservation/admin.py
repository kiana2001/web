from django.contrib import admin
from .models import Hotel, HotelBooking, City, Passenger

admin.site.register(Hotel)
admin.site.register(HotelBooking)
admin.site.register(City)
admin.site.register(Passenger)
