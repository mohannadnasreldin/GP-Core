# menu/serializers.py

from rest_framework import serializers
from .models import Menu, Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    food_items = RecipeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Menu
        fields = '__all__'
