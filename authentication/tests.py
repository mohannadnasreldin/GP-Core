# authentication/tests.py

import time
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        timestamp = str(int(time.time()))  # Unique timestamp
        self.user_data = {
            'username': 'testuser' + timestamp,
            'password': 'testpassword',
            'user_type': 'customer',
            'name': 'Test User',
            'age': 25,
            'address': 'Test Address',
            'email': 'test' + timestamp + '@example.com',
            'phone_no': '1234567890',
            'credit_info_customer': 'Test Credit Info',
            'preference': 'Test Preference',
        }
        CustomUser.objects.create_user(**self.user_data)
    def tearDown(self):
        CustomUser.objects.all().delete()
    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        try:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        except AssertionError:
            print(response.content)
            raise

        
    def test_login_user(self):
        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_register_user_incomplete_data(self):
        incomplete_data = {
            'username': 'incomplete_user',
            'password': 'incomplete_password',
            'user_type': 'customer',
            'name': 'Incomplete User',
            'email': 'incomplete@example.com',
        }
        response = self.client.post(self.register_url, incomplete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Change this line

    def test_login_user_invalid_credentials(self):
        invalid_login_data = {
            'username': 'testuser1',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, invalid_login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Change this line
