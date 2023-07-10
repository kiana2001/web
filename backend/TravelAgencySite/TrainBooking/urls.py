from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReservationCreateAPIView, TrainSearchView, ReservationListAPIView, TrainAPIView

urlpatterns = [
    path('trains/', TrainAPIView.as_view(), name='trains'),
    path('trains/search/', TrainSearchView.as_view(), name='train-search'),
    path('train-reservations/create', ReservationCreateAPIView.as_view(), name='reservation-create'),
    path('train-reservations/', ReservationListAPIView.as_view(), name='reservation-list'),
]