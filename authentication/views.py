# yourapp/views.py
import email
from rest_framework.response import Response
from rest_framework import status

from authentication.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class RegisterUser(APIView):
    def post(self, request, format='json'):
        # Check if the 'password' field is present in the request data
        if 'password' in request.data:
            # Hash the password before saving the user
            request.data['password'] = make_password(request.data['password'])

            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"password": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
# class LoginUser(APIView):
#     def post(self, request, format='json'):
#         email = request.data.get('email', None)
#         password = request.data.get('password', None)
        
#         try:
#             user = CustomUser.objects.get(email=email)
#         except CustomUser.DoesNotExist:
#             user = None

#         if user is not None and check_password(password, user.password):
#             return Response({'success': 'Login successful'})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class LoginUser(APIView):
    def post(self, request, format='json'):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None

        if user is not None:
            if check_password(password, user.password):
                return Response({'success': 'Login successful'})
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

