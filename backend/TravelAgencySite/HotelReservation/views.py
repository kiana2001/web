from rest_framework import viewsets, filters
from django.utils import timezone
from .models import Hotel, Room, HotelBooking
from .serializers import HotelSerializer, RoomSerializer, HotelReservationSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['hotel__name']  # Search by hotel name
    number_filter_fields = ['capacity']  # Filter by capacity

    def get_queryset(self):
        queryset = Room.objects.all()

        check_in_date = self.request.query_params.get('check_in_date')
        check_out_date = self.request.query_params.get('check_out_date')

        if check_in_date and check_out_date:
            # Filter rooms based on availability
            reserved_rooms = Reservation.objects.filter(
                check_in_date__lt=check_out_date,
                check_out_date__gt=check_in_date
            ).values_list('room_id', flat=True)

            queryset = queryset.exclude(id__in=reserved_rooms)

        return queryset


class HotelReservationViewSet(viewsets.ModelViewSet):
    queryset = HotelBooking.objects.all()
    serializer_class = HotelReservationSerializer

    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room')
        check_in_date = request.data.get('check_in_date')
        check_out_date = request.data.get('check_out_date')

        room = Room.objects.get(id=room_id)

        # Validate room availability
        reservations = HotelBooking.objects.filter(
            room=room,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date
        )

        if reservations.exists():
            return Response(
                {'error': 'Room is not available for the selected dates.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create the reservation
        reservation = HotelBooking.objects.create(
            user=request.user,
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date
        )

        serializer = self.get_serializer(reservation)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)