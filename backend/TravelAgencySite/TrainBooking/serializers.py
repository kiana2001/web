from rest_framework import serializers
from .models import Train, TrainReservation, Passenger
from FlightBooking.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):
    # origin = CitySerializer()
    # destination = CitySerializer()

    class Meta:
        model = Train
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class TrainReservationSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True)

    class Meta:
        model = TrainReservation
        exclude = ('user',)

    def validate(self, attrs):
        is_round_trip = attrs.get('is_round_trip')
        return_date = attrs.get('return_date')
        return_train = attrs.get('return_train')

        if is_round_trip and (not return_date or not return_train):
            raise serializers.ValidationError("return_date and return_train must have values when it is a round trip.")
        if attrs.get('train').origin == attrs.get('train').destination:
            raise serializers.ValidationError("origin and destination cannot be the same.")
        return attrs

    def create(self, validated_data):
        passengers_data = validated_data.pop('passengers')
        booking = Train.objects.create(**validated_data)
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