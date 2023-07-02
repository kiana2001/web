from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime
from pytz import timezone
from rest_framework.views import APIView

from .models import Train, TrainReservation
from .serializers import TrainSerializer, TrainReservationSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class TrainSearchView(APIView):
    def get(self, request):
        #localhost:8000/trains/search/?departure_city=Mashhad&arrival_city=Tehran&departure_date=2023-05-07&num_passengers=5
        #http://localhost:8000/trains/search/?departure_city=Tehran&arrival_city=Mashhad&departure_date=2023-07-05&num_passengers=5&is_round_trip=True&return_date=2023-07-03
        departure_city = self.request.query_params.get('departure_city')
        arrival_city = self.request.query_params.get('arrival_city')
        departure_date = self.request.query_params.get('departure_date')
        num_passengers = int(self.request.query_params.get('num_passengers', 1))
        is_round_trip = bool(self.request.query_params.get('is_round_trip', False))
        return_date = self.request.query_params.get('return_date', None)
        trains_outbound = Train.objects.filter(origin=departure_city,
                                                 destination=arrival_city,
                                                 departure_date=datetime.strptime(departure_date, '%Y-%m-%d').date(),
                                                 capacity__gte=num_passengers)
        serializer_outbound = TrainSerializer(trains_outbound, many=True)

        if is_round_trip:
            trains_return = Train.objects.filter(origin=arrival_city,
                                                   destination=departure_city,
                                                   departure_date=datetime.strptime(return_date,'%Y-%m-%d').date(),
                                                   capacity__gte=num_passengers)

            serializer_return = TrainSerializer(trains_return, many=True)

            return Response({
                'trains_outbound': serializer_outbound.data,
                'trains_return': serializer_return.data
            })

        return Response(serializer_outbound.data)

class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

class ReservationCreateAPIView(APIView):
    def post(self, request):
        serializer = TrainReservationSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)  # Raises a validation error if serializer is invalid
        reservation = serializer.save(user=self.request.user)

        train = reservation.train
        train.capacity -= (reservation.num_adults + reservation.num_children)
        train.save()

        num_adults = reservation.num_adults
        num_children = reservation.num_children
        total_price = float(train.price) * float(num_adults) + (0.5 * float(train.price) * float(num_children))

        if reservation.is_round_trip:
            return_train = reservation.return_train
            return_train.capacity -= (reservation.num_adults + reservation.num_children)
            return_train.save()
            total_price += float(return_train.price) * float(num_adults) + (
                        0.5 * float(return_train.price) * float(num_children))

        reservation.total_price = total_price
        reservation.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# {
#   "train": 1,
#   "is_round_trip": false,
#   "num_adults": 2,
#   "num_children": 0,
#   "return_train": null,
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
        reservations = TrainReservation.objects.filter(user=self.request.user)
        serializer = TrainReservationSerializer(reservations, many=True)
        return Response(serializer.data)
