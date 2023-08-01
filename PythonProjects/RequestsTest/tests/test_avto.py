import requests
import pytest

token = '3913ee8c58d2488c6a8b28500a48c497'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1380})
    assert response.status_code == 200


def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1380})
    assert response.json()['trainer_name'] == 'Рулер'
    