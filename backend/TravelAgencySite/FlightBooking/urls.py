from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReservationCreateAPIView, FlightSearchView, ReservationListAPIView, FlightViewSet

urlpatterns = [
   # path('flights/', FlightList.as_view(), name='flight-list'),
   # path('flights/<int:pk>/', FlightDetail.as_view(), name='flight-detail'),
    path('flights/', FlightViewSet.as_view({'get':'list'}), name='flights'),
    path('flights/search/', FlightSearchView.as_view(), name='flight-search'),
    path('flightreservations/create', ReservationCreateAPIView.as_view(), name='reservation-create'),
    path('flightreservations/', ReservationListAPIView.as_view(), name='reservation-list'),

    # path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
]