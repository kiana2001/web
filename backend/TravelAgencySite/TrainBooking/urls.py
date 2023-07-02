from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReservationCreateAPIView, TrainSearchView, ReservationListAPIView, TrainViewSet

urlpatterns = [
    path('trains/', TrainViewSet.as_view({'get':'list'}), name='trains'),
    path('trains/search/', TrainSearchView.as_view(), name='train-search'),
    path('train-reservations/create', ReservationCreateAPIView.as_view(), name='reservation-create'),
    path('train-reservations/', ReservationListAPIView.as_view(), name='reservation-list'),
]