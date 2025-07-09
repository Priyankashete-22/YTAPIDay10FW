import pytest
from utils.api_client import APIClient
import uuid

@pytest.fixture(scope="module")
def api_client():
    return APIClient()


def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
#Hi
#Hello
#Hello Priyanka Shete

'''def test_create_users(api_client):
    user_data = {
        "name": "Sudd",
        "username": "qa2 user",
        "email": "test2@gmail.com"
    }
    response = api_client.post("users", user_data)
    print(response.json())
    #assert response1.status_code == 201
    assert response.status_code == 201
    assert response.json()['name'] == "Sudd"
    id = response.json()['id']
    responseget = api_client.get("users/1")
    print(responseget.json())'''

#using json loader create data

def test_create_users(api_client, load_user_data):
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email
    response = api_client.post("users", user_data)
    print(response.json())
    #assert response1.status_code == 201
    assert response.status_code == 201
    assert response.json()['name'] == "Ridhan"
    id = response.json()['id']
    responseget = api_client.get("users/1")
    print(responseget.json())

def test_update_users(api_client):
    user_data = {
        "name": "Sudd K",
        "username": "qa2 user",
        "email": "test2@gmail.com"
    }
    response = api_client.put("users/1", user_data)
    print(response.json())
    #assert response1.status_code == 201
    assert response.status_code == 200
    assert response.json()['name'] == 'Sudd K'

def test_delete_users(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200
