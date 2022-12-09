from django.db import models

class Pokemon(models.Model):
    pkm_id = models.CharField(max_length=20, null=False, unique=True) # ID del pokemon que entrega la api
    name = models.CharField(max_length=100, unique=True) # Nombre del pokemon
    type = models.CharField(max_length=100, null=False) # tipo del pokemon
    height = models.IntegerField(null=False, default=0) # altura del pokemon
    weight = models.IntegerField(null=False, default=0) # peso del pokemon
    inverted_name= models.CharField(max_length=100, default="") # Nombre invertido del pokemon

