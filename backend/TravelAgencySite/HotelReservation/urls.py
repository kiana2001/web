from django.urls import path
from .views import HotelViewSet,CityViewSet, HotelSearchView, HotelReservationListAPIView, HotelDetailView, HotelReservationCreateAPIView

urlpatterns = [
    # Other URLs of your project
    path('hotels/', HotelViewSet.as_view({'get': 'list'}), name='hotel-list'),
    path('hotels/search', HotelSearchView.as_view(), name='hotel-list-search'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('locations/', CityViewSet.as_view({'get': 'list'}), name='locations'),
    path('hotel-reservations/', HotelReservationListAPIView.as_view(), name='hotel_reservations_list'),
    path('hotel-reservations/create/', HotelReservationCreateAPIView.as_view(), name='create_hotel_reservation')
]
