# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.models import Order, Review
from.serializers import ReviewSerializer, OrderSerializer
from rest_framework import viewsets
from.models import Product
from.serializers import ProductSerializer
from rest_framework.decorators import action
from .models import Product, Cart, CartProduct
from .serializers import ProductSerializer, CartSerializer, CartProductSerializer
from rest_framework import status


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        product = Product.objects.get(id=product_id)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_product.quantity += int(quantity)
        else:
            cart_product.quantity = quantity
        cart_product.save()

        return Response({'status': 'product added'})  
    

    @action(detail=True, methods=['post'])
    def remove_product(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')

        product = Product.objects.get(id=product_id)
        cart_product = CartProduct.objects.get(cart=cart, product=product)
        cart_product.delete()

        return Response({'status': 'product removed'})

        

@api_view(['GET', 'POST'])
def order_reviews(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(order=order)
            return Response({'message': 'Review created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = OrderSerializer(order, context={'request': request})
        return Response(serializer.data)
    




@api_view(['DELETE'])
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return Response({'message': 'Review deleted successfully'}, status=status.HTTP_200_OK)
