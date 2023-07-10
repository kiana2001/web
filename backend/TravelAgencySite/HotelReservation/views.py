from datetime import datetime
from rest_framework import viewsets, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = HotelReservationSerializer(data=request.data)
        if serializer.is_valid():
            num_passengers = int(request.data.get('no_of_guests', 1))
            check_in_date = datetime.strptime(request.data.get('checkin_date'), '%Y-%m-%d').date()
            check_out_date = datetime.strptime(request.data.get('checkout_date'), '%Y-%m-%d').date()
            reservation_duration = (check_out_date - check_in_date).days

            room_id = int(request.data.get("room"))
            room = get_object_or_404(Room, id=room_id)

            if room.capacity >= num_passengers:
                if room.is_available == False:
                    return Response({'error': "The room has been booked earlier"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    room.is_available = False
                    total_price_calculated = (room.price * reservation_duration)
                    room.save()
                    reservation = serializer.save(user=request.user, total_price=total_price_calculated)
                    reservation.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': "The room selected is not enough for the number of passengers you have"},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelReservationListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reservations = HotelBooking.objects.filter(user=self.request.user)
        serializer = HotelReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class HotelDetailView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
