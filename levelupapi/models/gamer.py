from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(User, max_length=155)
    email = models.CharField(User, max_length=155)