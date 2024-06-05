# serializers.py
from rest_framework import serializers
from .models import CartProduct
from.models import Order, Review,Product
from .models import Product, Cart, CartProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price',  'is_available',]




class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('product', 'quantity', 'cart')



class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(source='cartproduct_set', many=True)

    class Meta:
        model = Cart
        fields = ('__all__')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'order', 'rating', 'comment')


        

class OrderSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'product', 'quantity', 'total_price',  'reviews')







