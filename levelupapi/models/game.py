from django.db import models
from django.contrib.auth.models import User
from .game import Gamer
from .game_type import GameType


class Game(models.Model):
    name = models.CharField(max_length=50)
    gameTypeId = models.ForeignKey(GameType, on_delete=models.CASCADE)
    gamerId = models.ForeignKey(Gamer, on_delete=models.CASCADE)