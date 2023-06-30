from rest_framework import serializers
from .models import Hotel, Room, HotelBooking
from Users.serializers import UserSerializer

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields =('id','room_no','room_type','is_available',)

    
class HotelReservationSerializer(serializers.ModelSerializer):
   # guest=GuestSerializer
    room=RoomSerializer
    hotel=HotelSerializer
    class Meta:
        model= HotelBooking
        fields =('no_of_guests','hotel','checkin_date','checkout_date',)