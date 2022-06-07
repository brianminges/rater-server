from tkinter import CASCADE
from django.db import models
from raterprojectapi.models.gamer import Gamer
from raterprojectapi.models.game import Game

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    rating = models.IntegerField()