# # models.py
# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

# class Product(models.Model):
#     name = models.TextField(max_length=100, validators=[RegexValidator( regex='^[a-zA-Z]*$', message='Name should only contain alphabetic characters.')])
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     #image = models.ImageField(upload_to='products/')
#     is_available = models.BooleanField(default=True)
    



# class Cart(models.Model):
#     products = models.ManyToManyField(Product, through='CartProduct')



# class CartProduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    

#     def __str__(self):
#         return self.name




# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     #created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.product.name} - {self.quantity}"
    

# class Review(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     rating = models.CharField(max_length=100)
#     comment = models.TextField()

 
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings


class Product(models.Model):
    name = models.TextField(max_length=100, validators=[RegexValidator( regex='^[a-zA-Z]*$', message='Name should only contain alphabetic characters.')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #image = models.ImageField(upload_to='products/')
    is_available = models.BooleanField(default=True)

class Cart(models.Model):
    products = models.ManyToManyField(Product, through='CartProduct')

class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

class Review(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100)
    comment = models.TextField()

