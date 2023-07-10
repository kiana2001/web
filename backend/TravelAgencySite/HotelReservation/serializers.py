from rest_framework import serializers
from .models import Hotel, HotelBooking, Passenger, Room, City
from Users.serializers import UserSerializer

class HotelSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()

    def get_rooms(self, obj):
        rooms = Room.objects.filter(hotel=obj, is_available=True)
        serializer = RoomSerializer(rooms, many=True)
        return serializer.data

    class Meta:
        model = Hotel
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class HotelReservationSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True)
    total_price = serializers.ReadOnlyField()
    class Meta:
        model= HotelBooking
        fields =('no_of_guests', 'checkin_date','checkout_date','passengers', 'total_price', 'room', 'hotel')

    def create(self, validated_data):
        passengers_data = validated_data.pop('passengers')
        booking = HotelBooking.objects.create(**validated_data)
        for passenger_data in passengers_data:
            Passenger.objects.create(**passenger_data)
        return booking