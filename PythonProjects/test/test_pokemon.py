import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
token = '78e5e9b3ca6cb8af4f42550832bb8078'
header = {'Content-Type':'application/json', 'trainer_token' : token }
trainer_id = "33773"


def test_status_get_trainers():
    responce = requests.get(url = f'{URL}/trainers')
    assert responce.status_code == 200

def test_match_my_trainer_in_responce():
    responce_get_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id': trainer_id})
    assert responce_get_trainers.json()["data"][0]["id"] == trainer_id