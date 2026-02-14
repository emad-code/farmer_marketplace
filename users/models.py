from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

# Create your models here.
