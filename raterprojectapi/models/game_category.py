from django.db import models
from raterprojectapi.models.game import Game
from raterprojectapi.models.category import Category

class GameCategory(models.Model):
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)