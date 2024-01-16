import requests

token = "96af7be4eefc73f971d81c4fc80d11fb"

'''response_create= requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
                "name":"Tama",
                "photo":"https://dolnikov.ru/pokemons/albums/001.png"},
                headers={"Content-Type":"application/json",
                         "trainer_token": token,
            })

print(response_create.text)'''

'''response_rename= requests.put('https://api.pokemonbattle.me:9104/pokemons', json={
                "pokemon_id": "27613",
                "name": "Nuts",
                "photo": "https://dolnikov.ru/pokemons/albums/008.png"},
                headers={"Content-Type":"application/json",
                         "trainer_token": token,
            })
print(response_rename.text)'''

response_add_pokeball= requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json={
                "pokemon_id": "27613"},
                headers={"Content-Type":"application/json",
                         "trainer_token": token,
            })

print(response_add_pokeball.text)





'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": token,
    "email": "S781@yandex.ru",
    "password": "Den123"}, headers = {"Content-Type":"application/json"})

print(response.text)'''

'''response_activation = requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email',
                                    json={"trainer_token": token}, 
                                    headers = {"Content-Type":"application/json"})



print(response_activation.status_code)'''




'''if response_activation.status_code == 200:
    print('OK')
else:
    print('not ok')'''
    