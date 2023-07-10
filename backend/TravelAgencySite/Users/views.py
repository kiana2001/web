from django.middleware.csrf import get_token
from rest_framework.decorators import api_view, permission_classes, throttle_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer
from rest_framework.throttling import UserRateThrottle
import json
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Set session and cookie for the registered user
        response = Response(serializer.data)
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginThrottle(UserRateThrottle):
    rate = '10/minute'

@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([CustomLoginThrottle])
def login_api(request):
    username = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)

        response_data = {
            'message': 'Logged in successfully',
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }

        return Response(response_data)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def logout_api(request):
    response = Response({'message': 'Logged out successfully'})
    return response


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def profile_api(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
