# authentication/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('seller', 'Seller'),
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    username = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)

    # Fields specific to Customer
    credit_info_customer = models.CharField(max_length=50, blank=True, null=True)
    preference = models.CharField(max_length=50, blank=True, null=True)

    # Fields specific to Seller
    credit_info_seller = models.CharField(max_length=50, blank=True, null=True)

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
