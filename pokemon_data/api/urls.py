from django.urls import path
from .views import PokemonView, PokemonGetWeight, PokemonGetType, PokemonGetTypeHeight, PokemonGetInvertedName

urlpatterns = [
    path('home', PokemonView.as_view({'get': 'list'})),
    path('weight', PokemonGetWeight.as_view({'get': 'list'})),
    path('grass', PokemonGetType.as_view({'get': 'list'})),
    path('flying_10', PokemonGetTypeHeight.as_view({'get': 'list'})),
    path('inverted_name', PokemonGetInvertedName.as_view({'get': 'list'})),
    
]