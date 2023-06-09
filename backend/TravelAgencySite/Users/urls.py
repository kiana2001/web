from django.urls import path, include
from rest_framework import routers
from .views import login_api, logout_api, register_api, profile_api

urlpatterns = [
    path('login/', login_api, name='login'),
    path('logout/', logout_api, name='logout'),
    path('register/', register_api, name='register'),
    path('profile/', profile_api, name='profile')
]
