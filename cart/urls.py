# urls.py
from django.contrib import admin
from django.urls import path,include
from. import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
     path('router/', include(router.urls)),
    path('reviews/<int:order_id>/add', views.order_reviews, name='order_reviews'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),

]



