# yourapp/serializers.py
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'gender', 'credit_info_customer', 'preference', 'credit_info_seller', 'user_type', 'password']
