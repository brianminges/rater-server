from django.db import models

class Game(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    designer = models.CharField(max_length=50)
    released = models.DateField()
    num_of_players = models.IntegerField()
    age_recommended = models.IntegerField()