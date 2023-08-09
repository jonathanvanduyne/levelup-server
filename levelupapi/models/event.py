from django.db import models
from django.contrib.auth.models import User
from .game import Game
from .gamer import Gamer


class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)