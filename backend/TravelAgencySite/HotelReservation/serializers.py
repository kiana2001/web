from rest_framework import serializers
from .models import Hotel, HotelBooking, Passenger
from Users.serializers import UserSerializer

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class HotelReservationSerializer(serializers.ModelSerializer):
   # guest=GuestSerializer
    passengers = PassengerSerializer(many=True)
    class Meta:
        model= HotelBooking
        fields =('no_of_guests','hotel','checkin_date','checkout_date','passengers')

    def create(self, validated_data):
        passengers_data = validated_data.pop('passengers')
        booking = HotelBooking.objects.create(**validated_data)
        for passenger_data in passengers_data:
            Passenger.objects.create(**passenger_data)
        return booking