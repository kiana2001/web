from django.urls import path
from .views import HotelViewSet, RoomViewSet, HotelReservationViewSet

urlpatterns = [
    # Other URLs of your project
    path('hotels/', HotelViewSet.as_view({'get': 'list'}), name='hotel-list'),
    path('hotels/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve'}), name='hotel-detail'),
    path('rooms/', RoomViewSet.as_view({'get': 'list'}), name='room-list'),
    path('rooms/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve'}), name='room-detail'),
    path('hotelreservations/', HotelReservationViewSet.as_view({'get': 'list', 'post': 'create'}), name='reservation-list'),
    path('hotelreservations/<int:pk>/', HotelReservationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='reservation-detail'),
]
