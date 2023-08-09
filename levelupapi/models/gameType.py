from django.db import models
from django.contrib.auth.models import User


class GameType(models.Model):
    name = models.CharField(max_length=50)