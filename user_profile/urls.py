# urls.py
from django.urls import path
from .views import get_user_profile, update_user_profile

urlpatterns = [
    path('<int:user_id>/', get_user_profile, name='get_user_profile'),
    path('<int:user_id>/', update_user_profile, name='update_user_profile'),
    # Add other URL patterns as needed
]
