import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = '78e5e9b3ca6cb8af4f42550832bb8078'
header = {'Content-Type':'application/json', 'trainer_token' : token }
body_create_pokemon = {
                        "name": "generate",
                        "photo_id": -1
                      }




create_pokemon = requests.post(url = f'{URL}/pokemons', headers = header, json = body_create_pokemon )  # задание 1.1 создаю покемона
print(create_pokemon.json())                                                                            # вывожу в формате json

pokemon_id = create_pokemon.json()['id']                                                                # присваиваю id покемона новой переменной 

body_change_name_pokemon = {                                                                            # завожу новую переменную body с id уже созданного покемона
    "pokemon_id": pokemon_id,
    "name": "generate"
}

change_pokemon_name = requests.patch (url = f'{URL}/pokemons', headers = header, json = body_change_name_pokemon )  # задание 1.2 меняю имя покемона
print (change_pokemon_name.json())                                                                                  # вывожу в формате json

body_catch_pokemon = {
    "pokemon_id": pokemon_id
}

catch_pokemon = requests.post (url = f'{URL}/trainers/add_pokeball', headers = header, json = body_catch_pokemon )  # задание 1.3 поймать покемона в покебол
print (catch_pokemon.json())                                                                                        # вывожу в формате json      
