from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import UserSerializer
import json

@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Set session and cookie for the registered user
        request.session['user_id'] = user.id
        response = Response(serializer.data)
        response.set_cookie('user_id', user.id)
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    #data = json.loads(request.body)
    username = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Set session and cookie for the logged in user
        request.session['user_id'] = user.id
        response = Response({'message': 'Logged in successfully'})
        response.set_cookie('user_id', user.id)
        return response
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_api(request):
    logout(request)
    # Remove the session and cookie for the logged out user
    request.session.flush()
    response = Response({'message': 'Logged out successfully'})
    response.delete_cookie('user_id')
    return response


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
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
