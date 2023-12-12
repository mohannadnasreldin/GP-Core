from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.db import IntegrityError

class AdminOnlyPermission(permissions.BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        # Allow only admin to list users
        return request.user and request.user.is_authenticated and request.user.user_type == 'admin'

class RegisterUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'User with this username or email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        