from datetime import datetime

from rest_framework import viewsets, filters, status, generics
from django.utils import timezone
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Hotel, HotelBooking, City, Room
from .serializers import HotelSerializer, HotelReservationSerializer, CitySerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class HotelSearchView(APIView):
    def get(self, request):
        city = self.request.query_params.get('city')
        Hotels = Hotel.objects.filter(city__name=city)
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

            room_id = int(self.request.data.get("room"))
            room = get_object_or_404(Room, id=room_id)

            if room.capacity >= num_passengers:
                room.is_available = False
                total_price_calculated = (room.price * reservation_duration)
                room.save()
                reservation = serializer.save(user=self.request.user, total_price=total_price_calculated)
                reservation.save()
            else:
                return Response({'error':"The room selected is not enough for the number of passengers you have"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelReservationListAPIView(APIView):
    def get(self, request):
        reservations = HotelBooking.objects.filter(user=self.request.user)
        serializer = HotelReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class HotelDetailView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

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