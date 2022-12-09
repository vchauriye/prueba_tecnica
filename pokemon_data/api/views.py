from django.shortcuts import render
from rest_framework import generics
from .serializers import PkmnSerializer
from .models import Pokemon
from rest_framework import viewsets
from rest_framework.response import Response

# Se filtra por los primeros 50 Pokemon de la lista
class PokemonView(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()[:50]
    serializer_class = PkmnSerializer

# Se filtra por los Pokemon que pesen más de 30 y menos de 80
class PokemonGetWeight(viewsets.ViewSet):
    def list(self, request):
        queryset = Pokemon.objects.filter(weight__lt = 80, weight__gt = 30)
        serializer = PkmnSerializer(queryset, many=True)
        return Response(serializer.data)

# Se filtra por los Pokemon tipo “grass”
class PokemonGetType(viewsets.ViewSet):
    def list(self, request):
        queryset = Pokemon.objects.filter(type__contains='grass')
        serializer = PkmnSerializer(queryset, many=True)
        return Response(serializer.data)

# Se filtra por los Pokemon tipo “flying” que midan más de 10
class PokemonGetTypeHeight(viewsets.ViewSet):
    def list(self, request):
        queryset = Pokemon.objects.filter(type__contains='flying', height__gt =10 )
        serializer = PkmnSerializer(queryset, many=True)
        return Response(serializer.data)

# Se filtra por los Pokemon tipo “flying” que midan más de 10
class PokemonGetInvertedName(viewsets.ViewSet):
    def list(self, request):
        queryset = Pokemon.objects.all()
        serializer = PkmnSerializer(queryset, many=True)
        return Response(serializer.data)
    
    