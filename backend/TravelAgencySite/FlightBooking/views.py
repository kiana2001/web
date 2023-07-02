from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime
from pytz import timezone
from rest_framework.views import APIView

from .models import Flight, FlightReservation
from .serializers import FlightSerializer, FlightReservationSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class FlightSearchView(APIView):
    def get(self, request):
        #localhost:8000/flights/search/?departure_city=Mashhad&arrival_city=Tehran&departure_date=2023-05-07&num_passengers=5
        #http://localhost:8000/flights/search/?departure_city=Tehran&arrival_city=Mashhad&departure_date=2023-07-05&num_passengers=5&is_round_trip=True&return_date=2023-07-03
        departure_city = self.request.query_params.get('departure_city')
        arrival_city = self.request.query_params.get('arrival_city')
        departure_date = self.request.query_params.get('departure_date')
        num_passengers = int(self.request.query_params.get('num_passengers', 1))
        is_round_trip = bool(self.request.query_params.get('is_round_trip', False))
        return_date = self.request.query_params.get('return_date', None)
        flights_outbound = Flight.objects.filter(origin=departure_city,
                                                 destination=arrival_city,
                                                 departure_date=datetime.strptime(departure_date, '%Y-%m-%d').date(),
                                                 capacity__gte=num_passengers)
        serializer_outbound = FlightSerializer(flights_outbound, many=True)

        if is_round_trip:
            flights_return = Flight.objects.filter(origin=arrival_city,
                                                   destination=departure_city,
                                                   departure_date=datetime.strptime(return_date,'%Y-%m-%d').date(),
                                                   capacity__gte=num_passengers)

            serializer_return = FlightSerializer(flights_return, many=True)

            return Response({
                'flights_outbound': serializer_outbound.data,
                'flights_return': serializer_return.data
            })

        return Response(serializer_outbound.data)

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class ReservationCreateAPIView(APIView):
    def post(self, request):
        serializer = FlightReservationSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)  # Raises a validation error if serializer is invalid
        reservation = serializer.save(user=self.request.user)

        flight = reservation.flight
        flight.capacity -= (reservation.num_adults + reservation.num_children)
        flight.save()

        num_adults = reservation.num_adults
        num_children = reservation.num_children
        total_price = float(flight.price) * float(num_adults) + (0.5 * float(flight.price) * float(num_children))

        if reservation.is_round_trip:
            return_flight = reservation.return_flight
            return_flight.capacity -= (reservation.num_adults + reservation.num_children)
            return_flight.save()
            total_price += float(return_flight.price) * float(num_adults) + (
                        0.5 * float(return_flight.price) * float(num_children))

        reservation.total_price = total_price
        reservation.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# {
#   "flight": 1,
#   "is_round_trip": false,
#   "num_adults": 2,
#   "num_children": 0,
#   "return_flight": null,
#   "passengers": [
#     {
#       "ssn": "1234567890",
#       "first_name": "John",
#       "last_name": "Doe",
#       "is_adult": true
#     },
#     {
#       "ssn": "09878654321",
#       "first_name": "Jane",
#       "last_name": "Smith",
#       "is_adult": true
#     }
#   ]
# }


class ReservationListAPIView(APIView):
    def get(self, request):
        reservations = FlightReservation.objects.filter(user=self.request.user)
        serializer = FlightReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    #
    # def perform_create(self, serializer):
    #     reservation = serializer.save(user=self.request.user)
    #
    #     flight = reservation.flight
    #     flight.capacity -= (reservation.num_adults + reservation.num_children)
    #     flight.save()
    #
    #     num_adults = serializer.validated_data['num_adults']
    #     num_children = serializer.validated_data['num_children']
    #     total_price = float(flight.price) * float(num_adults) + (0.5 * float(flight.price) * float(num_children))
    #
    #     if reservation.is_round_trip:
    #         return_flight = reservation.return_flight
    #         return_flight.capacity -= (reservation.num_adults + reservation.num_children)
    #         return_flight.save()
    #         total_price += float(return_flight.price) * float(num_adults) + (0.5 * float(return_flight.price) * float(num_children))
    #
    #     # Assign the total_price value to the reservation object
    #     reservation.total_price = total_price
    #     reservation.save()
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# class ReservationList(generics.ListCreateAPIView):
#     serializer_class = FlightReservationSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return FlightReservation.objects.filter(user=user)
#
#     def create(self, request, *args, **kwargs):
#         # Deserialize request data
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         # Calculate total price based on flight prices and number of passengers
#
#         flights_data = serializer.validated_data.pop('flights')
#         flight_prices = [flight_data.price for flight_data in flights_data]
#         num_adults = serializer.validated_data['num_adults']
#         num_children = serializer.validated_data['num_children']
#         total_price = sum(flight_prices) * num_adults + (0.5 * sum(flight_prices) * num_children)
#         serializer.validated_data['total_price'] = total_price
#
#
#         # Create reservation object and save it to the database
#         reservation = FlightReservation.objects.create(**serializer.validated_data)
#         for flight_data in flights_data:
#             if not reservation.is_round_trip:
#                 reservation.flights.add(Flight.objects.get(id=flight_data.id))
#             else:
#                 flights = Flight.objects.filter(Q(id=flight_data.id) |
#                                                 (Q(departure_airport=flight_data.departure_airport) &
#                                                  Q(arrival_airport=flight_data.arrival_airport) &
#                                                  Q(departure_time__gte=reservation.return_date)))
#
#                 reservation.flights.add(*flights)
#
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


