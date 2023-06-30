from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime
from pytz import timezone
from rest_framework.views import APIView

from .models import Flight, FlightReservation
from .serializers import FlightSerializer, FlightReservationSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# class FlightList(generics.ListAPIView):
#     serializer_class = FlightSerializer
#
#     def get_queryset(self):
#         queryset = Flight.objects.all()
#
#         # Filter by departure airport
#         dep_airport = self.request.query_params.get('departure_airport', None)
#         if dep_airport is not None:
#             queryset = queryset.filter(departure_airport=dep_airport.upper())
#
#         # Filter by arrival airport
#         arr_airport = self.request.query_params.get('arrival_airport', None)
#         if arr_airport is not None:
#             queryset = queryset.filter(arrival_airport=arr_airport.upper())
#
#         # Filter by departure date
#         dep_date_str = self.request.query_params.get('departure_date', None)
#         if dep_date_str is not None:
#             try:
#                 dep_date = datetime.strptime(dep_date_str, '%Y-%m-%d')
#                 timezone_obj = timezone('US/Eastern')  # Set timezone to Eastern Standard Time by default
#                 dep_date = timezone_obj.localize(dep_date)
#
#                 # Filter flights that depart on or after the specified date
#                 queryset = queryset.filter(departure_time__gte=dep_date)
#             except ValueError:
#                 pass
#
#         # Filter by return date (for round trip)
#         return_date_str = self.request.query_params.get('return_date', None)
#         if return_date_str is not None:
#             try:
#                 return_date = datetime.strptime(return_date_str, '%Y-%m-%d')
#                 timezone_obj = timezone('US/Eastern')
#                 return_date = timezone_obj.localize(return_date)
#
#                 # Filter flights that arrive on or before the specified return date
#                 queryset = queryset.filter(arrival_time__lte=return_date)
#             except ValueError:
#                 pass
#
#         return queryset

class FlightSearchView(APIView):
    def get(self, request):
        departure_city = request.GET.get('departure_city')
        arrival_city = request.GET.get('arrival_city')
        departure_date = request.GET.get('departure_date')
        is_round_trip = bool(request.GET.get('is_round_trip', False))
        return_date = request.GET.get('return_date')
        num_passengers = int(request.GET.get('num_passengers', 1))
        flights_outbound = Flight.objects.filter(origin=departure_city,
                                                 destination=arrival_city,
                                                 departure_date=datetime.strptime(departure_date, '%Y-%m-%d').date(),
                                                 capacity__gte=num_passengers)
        serializer_outbound = FlightSerializer(flights_outbound, many=True)

        if is_round_trip:
            flights_return = Flight.objects.filter(origin=arrival_city,
                                                   destination=departure_city,
                                                   return_date=datetime.strptime(return_date,'%Y-%m-%d').date(),
                                                   capacity__gte=num_passengers)

            serializer_return = FlightSerializer(flights_return, many=True)

            return Response({
                'flights_outbound': serializer_outbound.data,
                'flights_return': serializer_return.data
            })

        return Response(serializer_outbound.data)

class FlightDetail(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class ReservationCreateAPIView(generics.CreateAPIView):
    queryset = FlightReservation.objects.all()
    serializer_class = FlightReservationSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


    def perform_create(self, serializer):
        reservation = serializer.save(user=self.request.user)

        flight = reservation.flight
        flight.capacity -= (reservation.num_adults + reservation.num_children)
        flight.save()

        num_adults = serializer.validated_data['num_adults']
        num_children = serializer.validated_data['num_children']
        total_price = float(flight.price) * float(num_adults) + (0.5 * float(flight.price) * float(num_children))

        if reservation.is_round_trip:
            return_flight = reservation.return_flight
            return_flight.capacity -= (reservation.num_adults + reservation.num_children)
            return_flight.save()
            total_price += float(return_flight.price) * float(num_adults) + (0.5 * float(return_flight.price) * float(num_children)) 

        # Assign the total_price value to the reservation object
        reservation.total_price = total_price
        reservation.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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


