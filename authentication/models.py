# authentication/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use Django's hashed password field
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255 , blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    # Fields specific to Customer
    credit_info_customer = models.CharField(max_length=50, blank=True, null=True)
    preference = models.CharField(max_length=50, blank=True, null=True)

    # Fields specific to Seller
    credit_info_seller = models.CharField(max_length=50, blank=True, null=True)

    # Add user_type field to represent the user's role or type
    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        # Add more choices as needed
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='customer')

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        related_query_name="user",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        related_query_name="user",
        blank=True,
        help_text="Specific permissions for this user.",
        error_messages={
            "add": "The permission you're trying to add already exists for the user.",
        },
    )

    def __str__(self):
        return f"{self.username} - {self.user_type}"
