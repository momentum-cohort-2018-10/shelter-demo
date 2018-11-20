from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Volunteer(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE)
    name = models.CharField("Legal name", max_length=255)
    skills = models.TextField("Special skills")
    phone_number = models.CharField("Best phone number", max_length=20)
