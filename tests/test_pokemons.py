
import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = "96af7be4eefc73f971d81c4fc80d11fb"

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 4065})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 4065})
    response = response.json()
    assert response.text["name"] == "prod"





'''def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 3788})
    assert response.status_code == 200

def test_part_of_body():
    response = requests.put(f'{host}/trainers', 
                            headers={"trainer_token":token},
                            json={
                            "name": "Den",
                            "city": "Tama"
                    })
    
    assert response.json["message"] == "Информация о тренере обновлена"

@pytest.mark.parametrize('key, value', [("trainer_name", "Den"),
                                        ("id", "3788"),
                                        ("city", "Tama")]) 
def test_response_json(key,value):
    response = requests.get(f'{host}/trainers', params={'tariner_id':3788})
    assert response.json[key] == value'''    



