# yourproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('profile/', include('user_profile.urls')),
    path('menu/', include('menu.urls')),
    #path('ml/', include('ml.urls')),
    path('cart/', include('cart.urls')),
    path('preference/', include('preference.urls')),
]
