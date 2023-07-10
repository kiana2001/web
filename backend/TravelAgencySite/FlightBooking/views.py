from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .models import Flight, FlightReservation
from .serializers import FlightSerializer, FlightReservationSerializer

class IsSpecialGroup(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            # Check if the user belongs to the special_group for POST requests
            return request.user.groups.filter(name='special_group').exists()
        else:
            return True

class FlightSearchView(APIView):
    def get(self, request):
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


class FlightViewSet(APIView):
    permission_classes = [IsSpecialGroup]

    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlightSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ReservationCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FlightReservationSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
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


class ReservationListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reservations = FlightReservation.objects.filter(user=self.request.user)
        serializer = FlightReservationSerializer(reservations, many=True)
        return Response(serializer.data)
