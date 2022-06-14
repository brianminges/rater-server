from django.db import models

from raterprojectapi.models.category import Category
from raterprojectapi.models.gamer import Gamer

class Game(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    designer = models.CharField(max_length=50)
    released = models.DateField()
    num_of_players = models.IntegerField()
    age_recommended = models.IntegerField()
    categories = models.ManyToManyField(to=Category)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
