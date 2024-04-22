from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    photo = models.ImageField(upload_to='user_photos/', default='default.jpg')
    username = models.CharField(max_length=150 ,unique=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='user_photos/', default='default.jpg')
    phone = models.CharField(max_length=15)
    address = models.TextField()
    country = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'address', 'country', 'bio']

    def __str__(self):
        return self.username
