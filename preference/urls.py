from django.urls import path
from .views import add_preference

urlpatterns = [
    path('<str:username>/<str:preference_value>/', add_preference, name='add_preference'),
]
