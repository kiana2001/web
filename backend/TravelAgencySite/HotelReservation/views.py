from datetime import datetime

from rest_framework import viewsets, filters, status
from django.utils import timezone
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Hotel, HotelBooking
from .serializers import HotelSerializer, HotelReservationSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelSearchView(APIView):
    def get(self, request):
        city = self.request.query_params.get('city')
        num_passengers = int(self.request.query_params.get('num_passengers'))
        Hotels = Hotel.objects.filter(city__name=city, capacity__gte=num_passengers)
        serializer_Hotels = HotelSerializer(Hotels, many=True)
        return Response(serializer_Hotels.data)

class HotelReservationCreateAPIView(APIView):
    def post(self, request):
        serializer = HotelReservationSerializer(data=request.data)
        if serializer.is_valid():
            num_passengers = int(request.data.get('no_of_guests', 1))
            check_in_date = datetime.strptime(self.request.data.get('checkin_date'), '%Y-%m-%d').date()
            check_out_date = datetime.strptime(self.request.data.get('checkout_date'), '%Y-%m-%d').date()
            reservation_duration = (check_out_date - check_in_date).days

            hotel_id = self.request.data.get("hotel")
            hotel = get_object_or_404(Hotel, id=hotel_id)

            if hotel.capacity >= num_passengers:
                # Decrease hotel capacity
                hotel.capacity -= num_passengers
                total_price_calculated = (hotel.price_per_person_daily * reservation_duration * num_passengers)
                hotel.save()
                reservation = serializer.save(user=self.request.user, total_price=total_price_calculated)
                reservation.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelReservationListAPIView(APIView):
    def get(self, request):
        reservations = HotelBooking.objects.filter(user=self.request.user)
        serializer = HotelReservationSerializer(reservations, many=True)
        return Response(serializer.data)


# class RoomViewSet(viewsets.ModelViewSet):
#     serializer_class = RoomSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['hotel__name']  # Search by hotel name
#     number_filter_fields = ['capacity']  # Filter by capacity
#
#     def get_queryset(self):
#         queryset = Room.objects.all()
#
#         check_in_date = self.request.query_params.get('check_in_date')
#         check_out_date = self.request.query_params.get('check_out_date')
#
#         if check_in_date and check_out_date:
#             # Filter rooms based on availability
#             reserved_rooms = Reservation.objects.filter(
#                 check_in_date__lt=check_out_date,
#                 check_out_date__gt=check_in_date
#             ).values_list('room_id', flat=True)
#
#             queryset = queryset.exclude(id__in=reserved_rooms)
#
#         return queryset


# class HotelReservationViewSet(viewsets.ModelViewSet):
#     queryset = HotelBooking.objects.all()
#     serializer_class = HotelReservationSerializer
#
#     def create(self, request, *args, **kwargs):
#         room_id = request.data.get('room')
#         check_in_date = request.data.get('check_in_date')
#         check_out_date = request.data.get('check_out_date')
#
#         room = Room.objects.get(id=room_id)
#
#         # Validate room availability
#         reservations = HotelBooking.objects.filter(
#             room=room,
#             check_in_date__lt=check_out_date,
#             check_out_date__gt=check_in_date
#         )
#
#         if reservations.exists():
#             return Response(
#                 {'error': 'Room is not available for the selected dates.'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         # Create the reservation
#         reservation = HotelBooking.objects.create(
#             user=request.user,
#             room=room,
#             check_in_date=check_in_date,
#             check_out_date=check_out_date
#         )
#
#         serializer = self.get_serializer(reservation)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)