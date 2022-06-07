from django.db import models
from raterprojectapi.models.gamer import Gamer
from raterprojectapi.models.game import Game

class Picture(models.Model):
    image = models.CharField(max_length=1000)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)