import requests
from pytest_voluptuous import S
from requests import Response

from schemas.requests_schema import create_user_schema, user_data_schema, login_successful_schema, \
    login_unsuccessful_schema, register_unsuccessful_user_schema


def test_register_user():
    response: Response = requests.get('https://reqres.in/api/users', params={'page': 2})
    assert response.status_code == 200
    assert response.json()['page'] == 2
    assert len(response.json()['data']) != 0


def test_create_user():
    name = 'Artem'
    job = 'QA'
    result = requests.post(
        url='https://reqres.in/api/users',
        json={
            "name": name,
            "job": job
        }
    )
    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user_schema)


def test_user_data():
    user_id = 7
    result = requests.get(
        url=f'https://reqres.in/api/users/{user_id}'
    )
    assert result.status_code == 200
    assert result.json() == S(user_data_schema)


def test_login_successful():
    login = 'eve.holt@reqres.in'
    password = 'cityslicka'
    result = requests.post(
        url='https://reqres.in/api/login',
        json={"email": login, "password": password},
    )
    assert result.status_code == 200
    assert result.json() == S(login_successful_schema)


def test_login_unsuccessful():
    login = 'QAS'
    password = 'limD!'
    result = requests.post(
        url='https://reqres.in/api/login',
        json={"email": login, "password": password},
    )
    assert result.status_code == 400
    assert result.json() == S(login_unsuccessful_schema)


def test_unsuccessful_user_registration():
    result = requests.post(
        url='https://reqres.in/api/register',
        json={"email": "sydney@fife"},
    )
    print(result)
    assert result.status_code == 400
    assert result.json() == S(register_unsuccessful_user_schema)
