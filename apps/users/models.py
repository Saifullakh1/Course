from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='profile')

    def __str__(self):
        return f"{self.username}"
