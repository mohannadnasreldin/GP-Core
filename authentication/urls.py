# yourapp/urls.py
from django.urls import path
from .views import  LoginUser,RegisterUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
]
