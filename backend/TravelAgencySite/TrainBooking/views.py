from rest_framework import generics, status, viewsets
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from datetime import datetime
from rest_framework.views import APIView
from .models import Train, TrainReservation
from .serializers import TrainSerializer, TrainReservationSerializer
from rest_framework.permissions import IsAuthenticated

class IsSpecialGroup(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            # Check if the user belongs to the special_group for POST requests
            return request.user.groups.filter(name='special_group').exists()
        else:
            return True


class TrainSearchView(APIView):
    def get(self, request):
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

class TrainAPIView(APIView):
    permission_classes = [IsSpecialGroup]

    def get(self, request):
        trains = Train.objects.all()
        serializer = TrainSerializer(trains, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TrainReservationSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
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

class ReservationListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reservations = TrainReservation.objects.filter(user=self.request.user)
        serializer = TrainReservationSerializer(reservations, many=True)
        return Response(serializer.data)
