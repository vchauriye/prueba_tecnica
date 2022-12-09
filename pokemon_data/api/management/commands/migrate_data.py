from django.core.management.base import BaseCommand
from ...models import Pokemon
import requests

class Command(BaseCommand):
    def handle(self, **options):
        Pokemon.objects.all().delete()

        all_pkm_url = []
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10000&offset=0')
        response = response.json()
        for pkm in response["results"]: 
            all_pkm_url.append(pkm["url"])

        all_pkm_info ={}
        for pkm in all_pkm_url:

            # Se realiza una segunda request con el url de cada pokemon para obetener toda su información
            # Se manejan los errores que puedan venir de la api
            response= requests.get(pkm)
            # response.raise_for_status() 
            if response.status_code != 204 or response.status_code != 503:
                response = response.json()

            # Debemos obetener el string del tipo del pokemon, y debemos 
            # ponernos en el caso que el pokemon tenga dos tipos
                types = []
                for t in response["types"]:
                    types.append(t["type"]["name"])
                if len(types) > 1:
                    pkm_type = types[0] + "/" + types[1]
                else:
                        pkm_type = types[0]
                
                # Sacamos la información que nos interesa de los pokemones
                
                pkm_data = Pokemon(
                    pkm_id = response["id"],
                    name = response["name"],
                    type = pkm_type,
                    height = response["height"],
                    weight = response["weight"],
                    inverted_name = response["name"][::-1]
                )
                pkm_data.save()
                # print(response["name"])