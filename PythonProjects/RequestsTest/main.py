import requests

token = '3913ee8c58d2488c6a8b28500a48c497'
host = 'https://api.pokemonbattle.me:9104'

response = requests.post(f'{host}/pokemons', 
                         json= {
    "name": "Бульбикус",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

if response.status_code == 200:
    json_response = response.json()
    print(json_response)
else:
    print(f"Ошибка {response.status_code}: {response.text}")




response = requests.put(f'{host}/pokemons', 
                        json={
    "pokemon_id": "5797",
    "name": "Шпинатуc",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

if response.status_code == 200:  
    json_response = response.json() 
    print(json_response)
else:
    print(f"Ошибка {response.status_code}: {response.text}")


response = requests.post(f'{host}/trainers/add_pokeball', 
                        json={
    "pokemon_id": "5796"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

if response.status_code == 200:  
    json_response = response.json() 
    print(json_response)
else:
    print(f"Ошибка {response.status_code}: {response.text}")