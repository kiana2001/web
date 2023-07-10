from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReservationCreateAPIView, FlightSearchView, ReservationListAPIView, FlightViewSet

urlpatterns = [
    path('flights/', FlightViewSet.as_view(), name='flights'),
    path('flights/search/', FlightSearchView.as_view(), name='flight-search'),
    path('flight-reservations/create', ReservationCreateAPIView.as_view(), name='reservation-create'),
    path('flight-reservations/', ReservationListAPIView.as_view(), name='reservation-list'),
]