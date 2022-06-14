"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game, Gamer, Category 
from django.core.exceptions import ValidationError

class GameView(ViewSet):
    """Gamer Rater game views"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single game
        
        Returns:
            Response -- JSON serialized game """
        
        try:
            game = Game.objects.get(pk=pk)
            # categories = game.gamecategory.all()
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle GET request for all games
        
        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        
        Returns:
            Response -- JSON serialized game instance
        """
        
        gamer = Gamer.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games""" 
    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'description',
            'designer',
            'released',
            'num_of_players',
            'age_recommended',
            'categories'
        )
        depth = 3      
        
class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'released', 'num_of_players', 'age_recommended')