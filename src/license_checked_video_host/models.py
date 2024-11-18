from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(max_length=200, null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
