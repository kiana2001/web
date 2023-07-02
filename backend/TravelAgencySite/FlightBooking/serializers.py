from rest_framework import serializers
from .models import City, Flight, FlightReservation, Passenger
from Users.serializers import UserSerializer


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    # origin = CitySerializer()
    # destination = CitySerializer()

    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = '__all__'
    
class FlightReservationSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True)

    class Meta:
        model = FlightReservation
        exclude = ('user',)

    def validate(self, attrs):
        is_round_trip = attrs.get('is_round_trip')
        return_date = attrs.get('return_date')
        return_flight = attrs.get('return_flight')

        if is_round_trip and (not return_date or not return_flight):
            raise serializers.ValidationError("return_date and return_flight must have values when it is a round trip.")
        if attrs.get('flight').origin == attrs.get('flight').destination:
            raise serializers.ValidationError("origin and destination cannot be the same.")
        return attrs

    def create(self, validated_data):
        passengers_data = validated_data.pop('passengers')
        booking = FlightReservation.objects.create(**validated_data)
        for passenger_data in passengers_data:
            ssn = passenger_data.get('ssn')
            try:
                passenger = Passenger.objects.get(ssn=ssn)
                for key, value in passenger_data.items():
                    setattr(passenger, key, value)
                passenger.is_adult = passenger_data.get('is_adult', True)  # Set default value if not provided
                passenger.save()
            except Passenger.DoesNotExist:
                passenger = Passenger.objects.create(**passenger_data)
            booking.passengers.add(passenger)
        return booking

# class FlightReservationSerializer(serializers.ModelSerializer):
#     flights = FlightSerializer(many=True)  # Add this line to show a list of flights in the reservation form
#
#     class Meta:
#         model = FlightReservation
#         fields = ['id', 'user', 'flights', 'is_round_trip', 'return_date', 'num_adults', 'num_children']
#
#     # def create(self, validated_data):
#     #     flights_data = validated_data.pop('flights')
#     #     reservation = FlightReservation.objects.create(**validated_data)
#     #     for flight_data in flights_data:
#     #         reservation.flights.add(flight_data['id'])
#     #    # reservation.total_price = calculate_total_price(reservation)  # You can define this function to calculate the total price
#     #     reservation.save()
#     #     return reservation

#class FlightMultipleChoiceField(serializers.PrimaryKeyRelatedField):
#    def get_queryset(self):
#        return Flight.objects.all()

#class FlightReservationSerializer(serializers.ModelSerializer):
#    flights = FlightMultipleChoiceField(many=True, queryset=Flight.objects.all())

#    class Meta:
 #       model = FlightReservation
 #       fields = ['id', 'user', 'flights', 'is_round_trip', 'return_date', 'num_adults', 'num_children']

    # def create(self, validated_data):
    #     flights_data = validated_data.pop('flights')
    #     reservation = FlightReservation.objects.create(**validated_data)
    #
    #     # Calculate total price based on flight prices and number of passengers
    #     flight_prices = [flight.price for flight in flights_data]
    #     num_adults = validated_data['num_adults']
    #     num_children = validated_data['num_children']
    #     total_price = sum(flight_prices) * num_adults + (0.5 * sum(flight_prices) * num_children)
    #     reservation.total_price = total_price
    #
    #     for flight_data in flights_data:
    #         reservation.flights.add(flight_data)
    #
    #     reservation.save()
    #     return reservation