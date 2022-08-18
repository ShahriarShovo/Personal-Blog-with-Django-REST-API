from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=20, unique=True)
    username=models.CharField(max_length=50, unique=True)

    REQUIRED_FIELDS=['email','phone']

    def __str__(self) -> str:
        return self.username

class Bio(models.Model):
    admin=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_image', null=True, blank=True)
    education=models.CharField(max_length=200,null=True, blank=True)
    profession=models.CharField(max_length=200,null=True, blank=True)
    about=models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.admin.username

