from django.db import models
from authentication.models import CustomUser
class Preference(models.Model):
    name = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
