
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menus/')
    


class Recipe(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='recipe/')
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Meta:
        app_label = 'menu'

# class UserInteraction(models.Model):
#     user_id = models.IntegerField()
#     recipe_id = models.IntegerField()
#     interaction_type = models.CharField(max_length=50)  # e.g., 'view', 'like', 'comment', etc.
#     timestamp = models.DateTimeField(auto_now_add=True)
